PY3_LIBRARY()

PY_SRCS(
    merge_coverage_inplace.py
)

PEERDIR(
    contrib/deprecated/python/ujson
    devtools/ya/exts
    devtools/ya/test/programs/test_tool/lib/coverage
    devtools/ya/test/util
)

END()

IF (OS_LINUX)
    RECURSE_FOR_TESTS(
        tests
    )
ENDIF()
