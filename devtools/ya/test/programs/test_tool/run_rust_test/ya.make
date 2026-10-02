PY3_LIBRARY()

PY_SRCS(
    run_rust_test.py
)

PEERDIR(
    devtools/ya/test/common
    devtools/ya/test/const
    devtools/ya/test/facility
    devtools/ya/test/filter
    devtools/ya/test/system/process
    devtools/ya/test/test_types
    devtools/ya/test/util
)

END()

RECURSE_FOR_TESTS(
    tests
)
