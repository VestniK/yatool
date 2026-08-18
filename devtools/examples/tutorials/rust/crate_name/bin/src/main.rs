// The name here is the module name the ya.make declares --
// RUST_CRATE(dashed_lib) -- not the directory.
use dashed_lib::answer;

fn main() {
    println!("The answer is {}", answer());
}
