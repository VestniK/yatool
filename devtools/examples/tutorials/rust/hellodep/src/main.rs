extern crate anyhow;

use std::io::stdin;

fn main() -> anyhow::Result<()> {
    println!("Give me a number:");
    let mut num = String::default();
    stdin().read_line(&mut num)?;
    let num = num.trim().parse::<i32>()?;
    println!("Your number is twice smaller than {}", 2 * num);
    Ok(())
}
