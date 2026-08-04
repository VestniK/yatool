RECURSE(
    cpp
    flatbuf
    go
    protobuf
    python
    java
)

# Only where build/platform/rust has a toolchain; see HAVE_RUST in
# build/conf/rust.conf.
IF (HAVE_RUST)
    RECURSE(rust)
ENDIF()
