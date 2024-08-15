#pragma once

#include "public.h"

#include <CXX/Objects.hxx> // pycxx

namespace NYT::NPython {

////////////////////////////////////////////////////////////////////////////////

Py::Exception CreateError(const Py::Callable& errorClass, const TString& message, const Py::Object& innerErrors);

Py::Exception CreateYtError(const TString& message, const Py::Object& innerErrors);
Py::Exception CreateYtError(const TString& message);

////////////////////////////////////////////////////////////////////////////////

Py::Exception CreateYsonError(const TString& message, const Py::Object& innerErrors);
Py::Exception CreateYsonError(const TString& message);

////////////////////////////////////////////////////////////////////////////////

} // namespace NYT::NPython
