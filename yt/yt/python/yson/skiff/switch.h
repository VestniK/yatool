#pragma once

#include "public.h"

#include <library/cpp/yt/memory/ref_counted.h>

#include <CXX/Extensions.hxx> // pycxx
#include <CXX/Objects.hxx> // pycxx

#include <util/generic/string.h>
#include <util/generic/hash.h>

namespace NYT::NPython {

////////////////////////////////////////////////////////////////////////////////

class TSkiffTableSwitchPython
    : public Py::PythonClass<TSkiffTableSwitchPython>
{
public:
    TSkiffTableSwitchPython(Py::PythonClassInstance* self, Py::Tuple& args, Py::Dict& kwargs);

    virtual ~TSkiffTableSwitchPython();

    ui16 GetTableIndex();

    static void InitType();

private:
    ui16 TableIndex_;
};

////////////////////////////////////////////////////////////////////////////////

} // namespace NYT::NPython
