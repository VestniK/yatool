#pragma once

#include <library/cpp/yt/memory/ref.h>

#include <util/stream/input.h>
#include <util/stream/output.h>
#include <util/stream/str.h>
#include <util/stream/zerocopy_output.h>

#include <CXX/Objects.hxx> // pycxx

#include <deque>

namespace NYT::NPython {

////////////////////////////////////////////////////////////////////////////////

std::unique_ptr<IZeroCopyInput> CreateInputStreamWrapper(const Py::Object& pythonInputStream, bool wrapPythonExceptions = false);

std::unique_ptr<IOutputStream> CreateOutputStreamWrapper(const Py::Object& pythonOutputStream, bool addBuffering);

std::unique_ptr<IZeroCopyOutput> CreateZeroCopyOutputStreamWrapper(const Py::Object& pythonOutputStream);

////////////////////////////////////////////////////////////////////////////////

std::unique_ptr<IZeroCopyInput> CreateOwningStringInput(TString string);

////////////////////////////////////////////////////////////////////////////////

class TStreamReader
{
public:
    static const size_t DefaultBlockSize_ = 1024 * 1024;

    TStreamReader();

    explicit TStreamReader(IInputStream* stream, size_t blockSize = DefaultBlockSize_);

    const char* Begin() const;
    const char* Current() const;
    const char* End() const;

    void RefreshBlock();
    void Advance(size_t bytes);

    bool IsFinished() const;
    TSharedRef ExtractPrefix(const char* endPtr);
    TSharedRef ExtractPrefix(size_t length);
    TSharedRef ExtractPrefix();

private:
    TSharedRef ExtractPrefix(int lastBlockIndex, const char* endPtr);

    IInputStream* Stream_;

    std::deque<TSharedRef> Blocks_;

    TSharedRef NextBlock_;
    i64 NextBlockSize_ = 0;

    const char* BeginPtr_ = nullptr;
    const char* CurrentPtr_ = nullptr;
    const char* EndPtr_ = nullptr;

    const char* PrefixStart_ = nullptr;

    bool Finished_ = false;

    size_t BlockSize_ = DefaultBlockSize_;

    void ReadNextBlock();
};

////////////////////////////////////////////////////////////////////////////////

} // namespace NYT::NPython

