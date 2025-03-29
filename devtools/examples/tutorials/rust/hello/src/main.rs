extern crate worldlib;

mod greet;

fn main() {
    greet::say_hello(worldlib::world_name());
}
