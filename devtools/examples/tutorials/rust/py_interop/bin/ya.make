PY3_PROGRAM(hello)

PY_SRCS(MAIN main.py)

SRCS(rustgreet.cpp)
PY_REGISTER(rustgreet)

PEERDIR(
    devtools/examples/tutorials/rust/py_interop/rslib
)

END()
