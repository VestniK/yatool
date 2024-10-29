#include "schema.h"

#include "error.h"
#include "record.h"
#include "../serialize.h"

#include <yt/yt/python/common/helpers.h>

#include <yt/yt/core/ytree/convert.h>
#include <yt/yt/core/ytree/fluent.h>

namespace NYT::NPython {

using namespace NYTree;
using namespace NSkiffExt;

////////////////////////////////////////////////////////////////////////////////

TSkiffSchema::TSkiffSchema(
    const std::shared_ptr<NSkiff::TSkiffSchema>& skiffSchema,
    const std::string& rangeIndexColumnName,
    const std::string& rowIndexColumnName)
    : SkiffSchema_(skiffSchema)
{
    TableDescription_ = CreateTableDescriptionList({skiffSchema}, rangeIndexColumnName, rowIndexColumnName)[0];

    ui16 index = 0;
    for (const auto& denseField : TableDescription_.DenseFieldDescriptionList)
    {
        FieldIndices_[denseField.Name()] = index;
        index += 1;
    }

    for (const auto& sparseField : TableDescription_.SparseFieldDescriptionList)
    {
        FieldIndices_[sparseField.Name()] = index;
        index += 1;
    }
}

TSkiffSchema::~TSkiffSchema() = default;

size_t TSkiffSchema::GetDenseFieldsCount()
{
    return TableDescription_.DenseFieldDescriptionList.size();
}

size_t TSkiffSchema::GetSparseFieldsCount()
{
    return TableDescription_.SparseFieldDescriptionList.size();
}

bool TSkiffSchema::HasOtherColumns()
{
    return TableDescription_.HasOtherColumns;
}

size_t TSkiffSchema::Size()
{
    return GetDenseFieldsCount() + GetSparseFieldsCount();
}

TFieldDescription TSkiffSchema::GetDenseField(ui16 index)
{
    return TableDescription_.DenseFieldDescriptionList[index];
}

TFieldDescription TSkiffSchema::GetSparseField(ui16 index)
{
    return TableDescription_.SparseFieldDescriptionList[index];
}

ui16 TSkiffSchema::GetFieldIndex(const TString& name)
{
    return FieldIndices_[name];
}

bool TSkiffSchema::HasField(const TString& name)
{
    return FieldIndices_.find(name) != FieldIndices_.end();
}

std::shared_ptr<NSkiff::TSkiffSchema> TSkiffSchema::GetSkiffSchema()
{
    return SkiffSchema_;
}

TIntrusivePtr<TSkiffRecord> TSkiffSchema::CreateNewRecord()
{
    return New<TSkiffRecord>(this);
}

////////////////////////////////////////////////////////////////////////////////

TSkiffSchemaPython::TSkiffSchemaPython(Py::PythonClassInstance* self, Py::Tuple& args, Py::Dict& kwargs)
    : Py::PythonClass<TSkiffSchemaPython>::PythonClass(self, args, kwargs)
{
    try {
        // Copy constructor.
        if (args.length() >= 1 && TSkiffSchemaPython::check(args.front())) {
            Py::PythonClassObject<TSkiffSchemaPython> skiffSchemaPythonObject(args.front());
            Schema_ = skiffSchemaPythonObject.getCxxObject()->GetSchemaObject();
            args = args.getSlice(1, args.length());
            ValidateArgumentsEmpty(args, kwargs);
            return;
        }

        auto schemaNode = ConvertToNode(ExtractArgument(args, kwargs, "table_skiff_schema"))->AsList();

        IMapNodePtr schemaRegistryNode;
        if (HasArgument(args, kwargs, "skiff_schema_registry")) {
            auto schemaRegistryArg = ExtractArgument(args, kwargs, "skiff_schema_registry");
            schemaRegistryNode = ConvertToNode(schemaRegistryArg)->AsMap();
        } else {
            schemaRegistryNode = BuildYsonNodeFluently()
                .BeginMap()
                .EndMap()
                ->AsMap();
        }

        auto skiffSchemas = ParseSkiffSchemas(schemaRegistryNode, schemaNode);
        if (skiffSchemas.size() != 1) {
            throw Py::ValueError("\"table_skiff_schema\" list should contain exactly one element");
        }

        TString rangeIndexColumnName = "@range_index";
        if (HasArgument(args, kwargs, "range_index_column_name")) {
            rangeIndexColumnName = Py::ConvertStringObjectToString(ExtractArgument(args, kwargs, "range_index_column_name"));
        }
        TString rowIndexColumnName = "@row_index";
        if (HasArgument(args, kwargs, "row_index_column_name")) {
            rowIndexColumnName = Py::ConvertStringObjectToString(ExtractArgument(args, kwargs, "row_index_column_name"));
        }

        ValidateArgumentsEmpty(args, kwargs);

        Schema_ = New<TSkiffSchema>(skiffSchemas[0], rangeIndexColumnName, rowIndexColumnName);
    } catch (const TErrorException& ex) {
        throw CreateSkiffError("Cannot create SkiffFormat", ex.Error());
    }
}

TSkiffSchemaPython::~TSkiffSchemaPython() = default;

int TSkiffSchemaPython::sequence_length()
{
    return Schema_->Size();
}

void TSkiffSchemaPython::InitType()
{
    behaviors().name("yt_yson_bindings.yson_lib.SkiffSchema");
    behaviors().doc("Skiff schema");

    behaviors().supportGetattro();
    behaviors().supportSetattro();

    PYCXX_ADD_NOARGS_METHOD(create_record, CreateRecord, "Create new record from schema");
    PYCXX_ADD_NOARGS_METHOD(has_other_columns, HasOtherColumns, "Check other columns presence");
    PYCXX_ADD_NOARGS_METHOD(__copy__, CopySchema, "Copy");
    PYCXX_ADD_NOARGS_METHOD(get_field_names, GetFieldNames, "Return field names");

    PYCXX_ADD_VARARGS_METHOD(__deepcopy__, DeepCopySchema, "Deepcopy");

    behaviors().readyType();
}

Py::Object TSkiffSchemaPython::CreateRecord()
{
    auto record = Schema_->CreateNewRecord();

    Py::Callable classType(TSkiffRecordPython::type());
    Py::PythonClassObject<TSkiffRecordPython> pythonObject(classType.apply(Py::TupleN(self()), Py::Dict()));

    auto cxxObject = pythonObject.getCxxObject();
    cxxObject->SetSkiffRecordObject(record);
    return pythonObject;
}

Py::Object TSkiffSchemaPython::HasOtherColumns()
{
    return Py::Boolean(Schema_->HasOtherColumns());
}

TIntrusivePtr<TSkiffSchema> TSkiffSchemaPython::GetSchemaObject()
{
    return Schema_;
}

Py::Object TSkiffSchemaPython::CopySchema()
{
    Py::Callable classType(TSkiffSchemaPython::type());
    Py::PythonClassObject<TSkiffSchemaPython> result(classType.apply(Py::TupleN(self()), Py::Dict()));
    return result;
}

Py::Object TSkiffSchemaPython::DeepCopySchema(const Py::Tuple& /*args*/)
{
    return CopySchema();
}

Py::Object TSkiffSchemaPython::GetFieldNames()
{
    Py::List result;

    for (ui16 index = 0; index < Schema_->GetDenseFieldsCount(); ++index) {
        auto field = Schema_->GetDenseField(index);
        result.append(Py::String(field.Name()));
    }

    for (ui16 index = Schema_->GetDenseFieldsCount(); index < Schema_->Size(); ++index) {
        auto field = Schema_->GetSparseField(index);
        result.append(Py::String(field.Name()));
    }
    return result;
}

////////////////////////////////////////////////////////////////////////////////

} // namespace NYT::NPython
