PY23_LIBRARY()

PY_SRCS(
    external_tools.py
    mds_storage.py
    sandbox_resource.py
    testdeps.py
    uid.py
)

PEERDIR(
    devtools/ya/core
    devtools/ya/core/imprint
    devtools/ya/exts
    devtools/ya/test/system/env
    devtools/ya/test/util
    devtools/ya/yalibrary/fetcher/http_client
    devtools/ya/yalibrary/large_files
    devtools/ya/yalibrary/platform_matcher
    devtools/ya/yalibrary/yandex/distbuild/distbs_consts
)

END()

RECURSE(
    sandbox_storage
)

RECURSE_FOR_TESTS(
    tests
)
