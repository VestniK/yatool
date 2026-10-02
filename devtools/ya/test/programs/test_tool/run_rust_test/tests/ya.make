PY3TEST()

PEERDIR(
    devtools/ya/test/programs/test_tool/run_rust_test
)

TEST_SRCS(
    test_parse_output.py
)

END()
