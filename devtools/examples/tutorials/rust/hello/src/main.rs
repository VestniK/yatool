mod greet;

// An external crate needs no `extern crate` declaration: every PEERDIR of the
// ya.make is already in scope by name, and a plain `use` pulls items out of it.
use worldlib::world_name;

fn main() {
    greet::say_hello(world_name());
}
