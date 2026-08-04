fn main() {
    // No `extern crate`, and the name here is CRATE_NAME, not the directory.
    println!("The answer is {}", dashed_lib::answer());
}
