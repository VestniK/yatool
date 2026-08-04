RUST_CRATE()

# The directory follows the crates.io spelling, the crate itself has to be a
# valid rust identifier. Without this the crate is unreachable: rustc resolves
# `-L` search paths by file name, never by crate metadata.
CRATE_NAME(dashed_lib)

END()
