#ifndef ROWS_ITERATOR_BASE_INL_H_
#error "Direct inclusion of this file is not allowed, include rows_iterator_base.h"
// For the sake of sane code completion.
#include "rows_iterator_base.h"
#endif

#include "error.h"

#include <yt/yt/core/misc/ref_counted_tracker.h>

namespace NYT::NPython {

////////////////////////////////////////////////////////////////////////////////

struct TRowsIteratorBufferTag { };

template <class TIteratorClass, class TConsumer, class TParser>
TRowsIteratorBase<TIteratorClass, TConsumer, TParser>::TRowsIteratorBase(
    Py::PythonClassInstance* self,
    Py::Tuple& args,
    Py::Dict& kwargs,
    const TString& formatName)
    : TBase::PythonClass(self, args, kwargs)
    , FormatName_(formatName)
    , Buffer_(GetRefCountedTypeCookie<TRowsIteratorBufferTag>(), BufferSize, /*initializeStorage*/ false)
{ }

template <class TIteratorClass, class TConsumer, class TParser>
Py::Object TRowsIteratorBase<TIteratorClass, TConsumer, TParser>::iter()
{
    return TBase::self();
}

template <class TIteratorClass, class TConsumer, class TParser>
PyObject* TRowsIteratorBase<TIteratorClass, TConsumer, TParser>::iternext()
{
    YT_VERIFY(InputStream_);
    YT_VERIFY(Consumer_);
    YT_VERIFY(Parser_);

    try {
        // Read unless we have the whole row.
        while (!Consumer_->HasObject() && !IsStreamExhausted_) {
            size_t length = InputStream_->Read(Buffer_.Begin(), BufferSize);
            if (length != 0) {
                Parser_->Read(TStringBuf(Buffer_.Begin(), length));
            }
            if (length != BufferSize) {
                IsStreamExhausted_ = true;
                Parser_->Finish();
            }
        }

        // Stop iteration if we are done.
        if (!Consumer_->HasObject()) {
            PyErr_SetNone(PyExc_StopIteration);
            return nullptr;
        }

        auto result = Consumer_->ExtractObject();
        // We should return pointer to alive object.
        result.increment_reference_count();
        return result.ptr();
    } CATCH_AND_CREATE_YSON_ERROR(FormatName_ + " load failed");
}

template <class TIteratorClass, class TConsumer, class TParser>
TRowsIteratorBase<TIteratorClass, TConsumer, TParser>::~TRowsIteratorBase() = default;

template <class TIteratorClass, class TConsumer, class TParser>
void TRowsIteratorBase<TIteratorClass, TConsumer, TParser>::InitType(const TString& formatName)
{
    Name_ = formatName + "Iterator";
    Doc_ = "Iterates over stream with " + formatName + " rows";
    TypeName_ = "yt_yson_bindings.yson_lib." + Name_;
    TBase::behaviors().name(TypeName_.c_str());
    TBase::behaviors().doc(Doc_.c_str());
    TBase::behaviors().supportGetattro();
    TBase::behaviors().supportSetattro();
    TBase::behaviors().supportIter();

    TBase::behaviors().readyType();
}

////////////////////////////////////////////////////////////////////////////////

} // namespace NYT::NPython
