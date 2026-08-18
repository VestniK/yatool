#include <Python.h>

// The rust staticlib is linked into this program like any other peer; the
// bridge below only turns its C ABI into something python can import.
extern "C" const char* py_greet_rs(const char*);
extern "C" void py_free_rs_string(const char*) noexcept;

namespace {

    PyObject* Greet(PyObject*, PyObject* args) {
        const char* name = nullptr;
        if (!PyArg_ParseTuple(args, "s", &name)) {
            return nullptr;
        }

        const char* msg = py_greet_rs(name);
        PyObject* res = PyUnicode_FromString(msg);
        py_free_rs_string(msg);
        return res;
    }

    PyMethodDef Methods[] = {
        {"greet", Greet, METH_VARARGS, "Greet the given name using the rust implementation."},
        {nullptr, nullptr, 0, nullptr},
    };

    PyModuleDef Module = {
        PyModuleDef_HEAD_INIT,
        "rustgreet",
        nullptr,
        -1,
        Methods,
        nullptr,
        nullptr,
        nullptr,
        nullptr,
    };

}

extern "C" PyObject* PyInit_rustgreet() {
    return PyModule_Create(&Module);
}
