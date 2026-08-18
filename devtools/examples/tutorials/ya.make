RECURSE(
    cpp
    flatbuf
    go
    protobuf
    python
    java
)

# Two conditions, and both are needed.
#
# HAVE_RUST (build/conf/rust.conf) answers whether build/platform/rust has a
# toolchain for this platform at all.
#
# BUILD_RUST_EXAMPLES is the opt-in. The rust modules are described with the
# `exclude` command modifier, which no released ymake knows yet, so configuring
# them with the ya that `./ya` downloads is a hard error -- and this ya.make is
# recursed into by everything that builds the tutorials. Until an ymake with
# `exclude` ships, building the examples is an explicit request:
#
#     ya make -DBUILD_RUST_EXAMPLES=yes --ymake-bin <built ymake> devtools/examples/tutorials/rust
#
# See build/platform/rust/README.md.
IF (HAVE_RUST AND BUILD_RUST_EXAMPLES)
    RECURSE(rust)
ENDIF()
