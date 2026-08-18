RUST_CRATE(dashed_lib)

# The directory follows the crates.io spelling, the crate itself has to be a
# valid rust identifier. The module-name argument covers both: it names the
# artifact (libdashed_lib.rlib), and the crate name follows it, so direct
# `--extern`s and rustc's transitive `-L` lookup -- which matches on the file
# name, never on crate metadata -- agree on what this crate is called.

END()
