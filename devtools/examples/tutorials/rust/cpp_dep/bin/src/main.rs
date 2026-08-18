use std::ffi::{CStr, CString};
use std::os::raw::c_char;

unsafe extern "C" {
    fn greet_cpp(name: *const c_char) -> *mut c_char;
    fn free_cpp_string(msg: *mut c_char);
}

fn main() {
    let name = CString::new("World").expect("The name is always a valid C string");
    let msg = unsafe { greet_cpp(name.as_ptr()) };
    assert!(!msg.is_null(), "Failed to allocate the greeting message");
    {
        let greeting = unsafe { CStr::from_ptr(msg) };
        println!("{}", greeting.to_str().expect("The message is always valid UTF8"));
    }
    unsafe { free_cpp_string(msg) };
}
