#include "stream.h"
#include "helpers.h"
#include "error.h"

#include <yt/yt/core/misc/blob_output.h>

#include <util/stream/buffered.h>
#include <util/stream/file.h>
#include <util/stream/zerocopy.h>

#include <string>

namespace NYT::NPython {

////////////////////////////////////////////////////////////////////////////////

class TInputStreamForwarder
    : public IZeroCopyInput
{
public:
    explicit TInputStreamForwarder(const Py::Object& inputStream, bool wrapPythonExceptions)
        : InputStream_(inputStream)
        , ReadFunction_(InputStream_.getAttr("read"))
        , LastReadResult_()
        , WrapPythonExceptions_(wrapPythonExceptions)
    { }

    virtual ~TInputStreamForwarder() noexcept = default;

    size_t DoNext(const void** ptr, size_t len) override
    {
        TGilGuard guard;

        auto args = Py::TupleN(Py::Long(static_cast<long>(std::min(BufferSize, len))));

        try {
            LastReadResult_ = ReadFunction_.apply(args);
        } catch (const Py::BaseException&) { \
            if (WrapPythonExceptions_) {
                THROW_ERROR Py::BuildErrorFromPythonException();
            } else {
                throw;
            }
        }

        PyObject* exception = PyErr_Occurred();
        if (exception) {
            if (WrapPythonExceptions_) {
                THROW_ERROR Py::BuildErrorFromPythonException();
            } else {
                throw Py::Exception();
            }
        }

#if PY_MAJOR_VERSION < 3
        // COMPAT: Due to implicit promotion to unicode it is sane to work with
        // unicode objects too.
        if (!PyBytes_Check(LastReadResult_.ptr()) && !PyUnicode_Check(LastReadResult_.ptr())) {
            throw Py::TypeError("Read returns non-string object");
        }
#else
        if (!PyBytes_Check(LastReadResult_.ptr())) {
            throw Py::TypeError("Input stream should be binary");
        }
#endif
        *ptr = PyBytes_AsString(*LastReadResult_);
        auto res = PyBytes_Size(*LastReadResult_);
        return res;
    }

private:
    Py::Object InputStream_;
    Py::Callable ReadFunction_;
    Py::Object LastReadResult_;

    static constexpr size_t BufferSize = 64_KB;

    const bool WrapPythonExceptions_;
};

std::unique_ptr<IZeroCopyInput> CreateInputStreamWrapper(const Py::Object& pythonInputStream, bool wrapPythonExceptions)
{
#if PY_MAJOR_VERSION < 3
    if (PyFile_Check(pythonInputStream.ptr())) {
        FILE* file = PyFile_AsFile(pythonInputStream.ptr());
        return std::make_unique<TFileInput>(Duplicate(file));
    } else {
        return std::make_unique<TInputStreamForwarder>(pythonInputStream, wrapPythonExceptions);
    }
#else
    return std::make_unique<TInputStreamForwarder>(pythonInputStream, wrapPythonExceptions);
#endif
}

////////////////////////////////////////////////////////////////////////////////

template <typename TFun>
void RunWithPossiblePythonException(TStringBuf description, TFun fun)
{
    PyObject *errorType, *errorValue, *errorTraceback;
    PyErr_Fetch(&errorType, &errorValue, &errorTraceback);

    try {
        fun();
    } catch (const Py::BaseException& pyException) {
        if (!errorType) {
            throw;
        }
        Cerr << "Exception raised inside " << description << " while handling exception:\n";
        PyErr_Print();
    }

    PyErr_Restore(errorType, errorValue, errorTraceback);
}

class TOutputStreamForwarder
    : public IOutputStream
{
public:
    explicit TOutputStreamForwarder(const Py::Object& outputStream)
        : OutputStream_(outputStream)
        , WriteFunction_(OutputStream_.getAttr("write"))
    { }

    virtual ~TOutputStreamForwarder() noexcept = default;

    void DoWrite(const void* buf, size_t len) override
    {
        TGilGuard guard;

        RunWithPossiblePythonException("TOutputStreamForwarder::DoWrite", [&] {
            size_t index = 0;
            while (len > 0) {
                // NB: python string interface uses i32 for length.
                size_t toWrite = std::min(len, static_cast<size_t>(1_GB));
                WriteFunction_.apply(Py::TupleN(Py::Bytes(
                    reinterpret_cast<const char*>(buf) + index,
                    toWrite)));
                len -= toWrite;
                index += toWrite;
            }
        });
    }

private:
    Py::Object OutputStream_;
    Py::Callable WriteFunction_;
};

class TBufferedStreamWrapper
    : public IZeroCopyOutput
{
public:
    explicit TBufferedStreamWrapper(std::unique_ptr<IOutputStream> outputStreamHolder)
        : UnderlyingOutputStream_(std::move(outputStreamHolder))
        , BufferedOutputStream_(UnderlyingOutputStream_.get(), 1_MB)
    { }

    void DoWrite(const void* buf, size_t len) override
    {
        BufferedOutputStream_.Write(buf, len);
    }

    size_t DoNext(void** ptr) override
    {
        return BufferedOutputStream_.Next(ptr);
    }

    void DoUndo(size_t len) override
    {
        BufferedOutputStream_.Undo(len);
    }

private:
    std::unique_ptr<IOutputStream> UnderlyingOutputStream_;
    TBufferedOutput BufferedOutputStream_;
};

std::unique_ptr<IOutputStream> CreateOutputStreamWrapper(const Py::Object& pythonOutputStream, bool addBuffering)
{
#if PY_MAJOR_VERSION < 3
    std::unique_ptr<IOutputStream> outputStreamHolder;
    if (PyFile_Check(pythonOutputStream.ptr())) {
        FILE* file = PyFile_AsFile(pythonOutputStream.ptr());
        outputStreamHolder = std::make_unique<TFileOutput>(Duplicate(file));
    } else {
        outputStreamHolder = std::make_unique<TOutputStreamForwarder>(pythonOutputStream);
    }
    if (addBuffering) {
        return std::make_unique<TBufferedStreamWrapper>(std::move(outputStreamHolder));
    } else {
        return outputStreamHolder;
    }
#else
    Y_UNUSED(addBuffering);
    // Python 3 has "io" module with fine-grained buffering control, no need in
    // additional buferring here.
    return std::unique_ptr<TOutputStreamForwarder>(new TOutputStreamForwarder(pythonOutputStream));
#endif
}

std::unique_ptr<IZeroCopyOutput> CreateZeroCopyOutputStreamWrapper(const Py::Object& pythonOutputStream)
{
    return std::make_unique<TBufferedStreamWrapper>(CreateOutputStreamWrapper(pythonOutputStream, false));
}

////////////////////////////////////////////////////////////////////////////////

class TOwningStringInput
    : public IZeroCopyInput
{
public:
    explicit TOwningStringInput(TString string)
        : String_(std::move(string))
        , Stream_(String_)
    { }

private:
    size_t DoNext(const void** ptr, size_t len) override
    {
        return Stream_.Next(ptr, len);
    }

    TString String_;
    TStringInput Stream_;
};

std::unique_ptr<IZeroCopyInput> CreateOwningStringInput(TString string)
{
    return std::unique_ptr<IZeroCopyInput>(new TOwningStringInput(string));
}

////////////////////////////////////////////////////////////////////////////////

struct TInputStreamBlobTag { };

TStreamReader::TStreamReader()
{ }

TStreamReader::TStreamReader(IInputStream* stream, size_t blockSize)
    : Stream_(stream)
    , BlockSize_(blockSize)
{
    ReadNextBlock();
    if (!Finished_) {
        RefreshBlock();
    }
}

const char* TStreamReader::Begin() const
{
    return BeginPtr_;
}

const char* TStreamReader::Current() const
{
    return CurrentPtr_;
}

const char* TStreamReader::End() const
{
    return EndPtr_;
}

void TStreamReader::RefreshBlock()
{
    YT_VERIFY(CurrentPtr_ == EndPtr_);
    YT_VERIFY(!Finished_);

    Blocks_.push_back(NextBlock_);
    if (Blocks_.size() == 1) {
        PrefixStart_ = Blocks_[0].begin();
    }

    BeginPtr_ = NextBlock_.Begin();
    CurrentPtr_ = BeginPtr_;
    EndPtr_ = NextBlock_.Begin() + NextBlockSize_;

    if (NextBlockSize_ < static_cast<ssize_t>(BlockSize_)) {
        Finished_ = true;
    } else {
        ReadNextBlock();
    }
}

void TStreamReader::Advance(size_t bytes)
{
    CurrentPtr_ += bytes;
}

bool TStreamReader::IsFinished() const
{
    return Finished_;
}

TSharedRef TStreamReader::ExtractPrefix(int endBlockIndex, const char* endPtr)
{
    TSharedRef result;

    if (endBlockIndex == 0) {
        result = Blocks_[0].Slice(PrefixStart_, endPtr);
    } else {
        auto firstBlockSuffixLength = Blocks_[0].End() - PrefixStart_;
        auto lastBlockPrefixLength = endPtr - Blocks_[endBlockIndex].Begin();
        auto prefixLength = firstBlockSuffixLength + (endBlockIndex - 1) * BlockSize_ + lastBlockPrefixLength;
        TBlobOutput prefixOutput(prefixLength);

        prefixOutput.Write(PrefixStart_, firstBlockSuffixLength);
        for (int i = 1; i < endBlockIndex; ++i) {
            prefixOutput.Write(Blocks_[i].Begin(), Blocks_[i].Size());
        }
        prefixOutput.Write(Blocks_[endBlockIndex].Begin(), lastBlockPrefixLength);

        Blocks_.erase(Blocks_.begin(), Blocks_.begin() + endBlockIndex);
        result = prefixOutput.Flush();
    }

    PrefixStart_ = endPtr;
    YT_VERIFY(Blocks_[0].begin() <= PrefixStart_ && PrefixStart_ <= Blocks_[0].end());

    return result;
}

TSharedRef TStreamReader::ExtractPrefix(const char* endPtr)
{
    if (Blocks_.empty()) {
        return TSharedRef();
    }

    for (int i = 0; i < std::ssize(Blocks_); ++i) {
        if (endPtr >= Blocks_[i].Begin() && endPtr <= Blocks_[i].End()) {
            return ExtractPrefix(i, endPtr);
        }
    }

    YT_ABORT();
}

TSharedRef TStreamReader::ExtractPrefix()
{
    return ExtractPrefix(CurrentPtr_);
}

TSharedRef TStreamReader::ExtractPrefix(size_t length)
{
    if (Blocks_.empty()) {
        return TSharedRef();
    }

    auto firstBlockSuffixLength = Blocks_[0].End() - PrefixStart_;
    if (static_cast<ssize_t>(length) <= firstBlockSuffixLength) {
        return ExtractPrefix(0, PrefixStart_ + length);
    }

    length -= firstBlockSuffixLength;
    int lastBlockIndex;
    int positionInLastBlock = length % BlockSize_;
    if (positionInLastBlock == 0) {
        lastBlockIndex = length / BlockSize_;
        positionInLastBlock = BlockSize_;
    } else {
        lastBlockIndex = length / BlockSize_ + 1;
    }

    YT_VERIFY(lastBlockIndex < std::ssize(Blocks_));
    return ExtractPrefix(lastBlockIndex, Blocks_[lastBlockIndex].Begin() + positionInLastBlock);
}

void TStreamReader::ReadNextBlock()
{
    auto block = TSharedMutableRef::Allocate<TInputStreamBlobTag>(BlockSize_, {.InitializeStorage = false});
    NextBlockSize_ = Stream_->Load(block.Begin(), block.Size());
    NextBlock_ = block;
    if (NextBlockSize_ == 0) {
        Finished_ = true;
    }
}

////////////////////////////////////////////////////////////////////////////////

} // namespace NYT::NPython
