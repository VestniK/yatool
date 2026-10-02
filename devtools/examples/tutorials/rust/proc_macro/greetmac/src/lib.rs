extern crate proc_macro;

use proc_macro::TokenStream;

/// Generates `fn greet() -> String` returning a greeting for the given name.
///
/// Runs inside the compiler while the consumer is being built, which is what
/// makes this module a host artifact rather than something linked into the
/// resulting program.
#[proc_macro]
pub fn greet_with(item: TokenStream) -> TokenStream {
    let name = item.to_string();
    let name = name.trim().trim_matches('"');
    format!("fn greet() -> String {{ format!(\"Hello dear {}!\") }}", name)
        .parse()
        .expect("The generated function is always valid rust")
}
