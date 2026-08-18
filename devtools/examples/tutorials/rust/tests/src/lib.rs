// A RUST_TEST module holds the tests, not the code under test -- the same
// shape as cargo's tests/*.rs. `ya make -t` builds this crate with
// `rustc --test` and runs every #[test] function as a testcase.
use worldlib::world_name;

#[test]
fn world_has_a_name() {
    assert_eq!(world_name(), "World");
}

#[test]
fn name_is_not_empty() {
    assert!(!world_name().is_empty());
}
