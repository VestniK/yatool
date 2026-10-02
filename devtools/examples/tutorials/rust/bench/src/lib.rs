// #[bench] needs the perma-unstable `test` crate, so RUST_BENCH compiles with
// RUSTC_BOOTSTRAP=1 -- that is what lets a stable rustc accept the feature
// gate below. `ya make -t` runs the binary with --bench and reports each
// benchmark's ns/iter as test metrics.
#![feature(test)]

extern crate test;

use test::Bencher;
use worldlib::world_name;

#[bench]
fn bench_world_name(b: &mut Bencher) {
    b.iter(|| test::black_box(world_name()).len());
}
