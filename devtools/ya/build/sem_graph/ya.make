PY3_LIBRARY()

PY_SRCS(
    __init__.py
)

PEERDIR(
    devtools/ya/core/config
    devtools/ya/build/build_facade
    devtools/ya/build/ymake2
    devtools/ya/yalibrary/sjson
    devtools/ya/yalibrary/tools
)

END()
