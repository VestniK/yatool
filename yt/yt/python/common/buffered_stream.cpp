#include "buffered_stream.h"
#include "helpers.h"

#include <mutex>

namespace NYT::NPython {

////////////////////////////////////////////////////////////////////////////////

TBufferedStream::TBufferedStream(size_t capacity)
    : Data_(TSharedMutableRef::Allocate(capacity, {.InitializeStorage = false}))
    , Begin_(Data_.Begin())
    , Capacity_(capacity)
    , AllowReadPromise_(NewPromise<void>())
    , AllowWritePromise_(NewPromise<void>())
{ }

size_t TBufferedStream::WaitDataToRead(size_t size)
{
    TGuard<TMutex> guard(ReadMutex_);

    bool wait = false;

    {
        TGuard<TMutex> guard(Mutex_);

        if (Size_ < size) {
            SizeToRead_ = size;
            Capacity_ = std::max(Capacity_, size * 2);
            if (Full_) {
                Full_ = false;
                AllowWritePromise_.Set(TError());
            }
            if (!Finished_) {
                wait = true;
                AllowReadPromise_ = NewPromise<void>();
                AllowReadCookie_ = RegisterFuture(AllowReadPromise_);
                if (AllowReadCookie_ == InvalidFutureCookie) { // Finalization started.
                    return 0;
                }
            }
        }
    }

    if (wait) {
        // Busy wait.
        auto future = AllowReadPromise_.ToFuture();
        auto result = WaitForSettingFuture(future);
        if (!result) { // Some error occurred.
            return 0;
        }
        if (!future.Get().IsOK()) { // Finalization is in progress.
            return 0;
        }
        UnregisterFuture(AllowReadCookie_);
    }

    {
        TGuard<TMutex> guard(Mutex_);
        return std::min(size, Size_);
    }
}

void TBufferedStream::Read(size_t size, char* dest)
{
    TGuard<TMutex> guard(ReadMutex_);

    YT_VERIFY(Size_ >= size);

    SizeToRead_ = 0;

    memcpy(dest, Begin_, size);
    Begin_ += size;
    Size_ -= size;

    if (Size_ * 2 < Capacity_ && Full_) {
        Full_ = false;
        AllowWritePromise_.Set(TError());
    }
}

bool TBufferedStream::Empty() const
{
    TGuard<TMutex> guard(Mutex_);
    return Finished_ && Size_ == 0;
}

void TBufferedStream::Finish()
{
    TGuard<TMutex> guard(Mutex_);

    YT_VERIFY(!Finished_);

    Finished_ = true;

    AllowReadPromise_.TrySet(TError());
}

TFuture<void> TBufferedStream::Close()
{
    Finish();
    return VoidFuture;
}

TFuture<void> TBufferedStream::Write(const TSharedRef& data)
{
    TGuard<TMutex> guard(Mutex_);

    YT_VERIFY(!Finished_);

    {
        if (Data_.End() < Begin_ + Size_ + data.Size()) {
            if (Size_ + data.Size() > Data_.Size()) {
                Reallocate(std::max(Size_ + data.Size(), Data_.Size() * 2));
            } else if (static_cast<ssize_t>(Size_) <= Begin_ - Data_.Begin()) {
                Move(Data_.Begin());
            } else {
                Reallocate(Data_.Size());
            }
        }

        std::copy(data.Begin(), data.Begin() + data.Size(), Begin_ + Size_);
        Size_ += data.Size();
    }

    if (Size_ >= SizeToRead_) {
        AllowReadPromise_.TrySet(TError());
    }

    if (Capacity_ <= Size_ * 2) {
        Full_ = true;
        AllowWritePromise_ = NewPromise<void>();
        return AllowWritePromise_
            .ToFuture()
            .ToImmediatelyCancelable();
    } else {
        return VoidFuture;
    }
}

TFuture<void> TBufferedStream::Flush()
{
    return VoidFuture;
}

void TBufferedStream::Reallocate(size_t len)
{
    YT_VERIFY(len >= Size_);

    auto newData = TSharedMutableRef::Allocate(len, {.InitializeStorage = false});
    Move(newData.Begin());
    std::swap(Data_, newData);
}

void TBufferedStream::Move(char* dest)
{
    std::copy(Begin_, Begin_ + Size_, dest);
    Begin_ = dest;
}

////////////////////////////////////////////////////////////////////////////////

TString TBufferedStreamWrap::TypeName_;

TBufferedStreamWrap::TBufferedStreamWrap(Py::PythonClassInstance *self, Py::Tuple& args, Py::Dict& kwargs)
    : Py::PythonClass<TBufferedStreamWrap>::PythonClass(self, args, kwargs)
    , Stream_(New<TBufferedStream>(Py::ConvertToLongLong(ExtractArgument(args, kwargs, "size"))))
{
    ValidateArgumentsEmpty(args, kwargs);
}

Py::Object TBufferedStreamWrap::Read(Py::Tuple& args, Py::Dict& kwargs)
{
    auto size = Py::ConvertToLongLong(ExtractArgument(args, kwargs, "size"));
    ValidateArgumentsEmpty(args, kwargs);

    // Shrink size to available data size if stream has finished.
    {
        TReleaseAcquireGilGuard guard;
        size = Stream_->WaitDataToRead(size);
    }

    if (PyErr_Occurred()) {
        throw Py::Exception();
    }

#if PY_MAJOR_VERSION >= 3
    auto* rawResult = PyBytes_FromStringAndSize(nullptr, size);
    char* underlyingString = PyBytes_AsString(rawResult);
#else
    auto* rawResult = PyString_FromStringAndSize(nullptr, size);
    char* underlyingString = PyBytes_AsString(rawResult);
#endif

    {
        TReleaseAcquireGilGuard guard;
        Stream_->Read(size, underlyingString);
    }

    return Py::Object(rawResult, true);
}

Py::Object TBufferedStreamWrap::Empty(Py::Tuple& args, Py::Dict& kwargs)
{
    ValidateArgumentsEmpty(args, kwargs);

    bool empty;
    {
        TReleaseAcquireGilGuard guard;
        empty = Stream_->Empty();
    }
    return Py::Boolean(empty);
}

TBufferedStreamPtr TBufferedStreamWrap::GetStream()
{
    return Stream_;
}

TBufferedStreamWrap::~TBufferedStreamWrap()
{ }

void TBufferedStreamWrap::InitType(const TString& moduleName)
{
    static std::once_flag flag;
    std::call_once(flag, [&] {
        TypeName_ = moduleName + ".BufferedStream";
        behaviors().name(TypeName_.c_str());
        behaviors().doc("Buffered stream to perform read and download asynchronously");
        behaviors().supportGetattro();
        behaviors().supportSetattro();

        PYCXX_ADD_KEYWORDS_METHOD(read, Read, "Synchronously read data from stream");
        PYCXX_ADD_KEYWORDS_METHOD(empty, Empty, "Check that the stream is empty");

        behaviors().readyType();
    });
}

////////////////////////////////////////////////////////////////////////////////

} // namespace NYT::NPython
