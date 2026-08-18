use std::ffi::{CStr, CString};
use std::io::Write;
use std::os::raw::c_char;

unsafe extern "C" {
    fn greet_cpp(name: *const c_char) -> *mut c_char;
    fn free_cpp_string(msg: *mut c_char);
}

/// Wraps the greeting produced by the C++ peer into one more layer.
///
/// # Safety
/// `name` must be a valid pointer to a NUL-terminated UTF8 string.
#[unsafe(no_mangle)]
pub unsafe extern "C" fn sandwich_greet(name: *const c_char) -> *const c_char {
    let inner = unsafe { greet_cpp(name) };
    assert!(!inner.is_null(), "Failed to allocate the greeting message");
    let inner_str = unsafe { CStr::from_ptr(inner) }
        .to_str()
        .expect("The message is always valid UTF8")
        .to_owned();
    unsafe { free_cpp_string(inner) };

    let mut res_data = Vec::<u8>::default();
    write!(&mut res_data, "Rust saw: {}", inner_str).expect("Failed to write greeting message");
    CString::new(res_data)
        .expect("CString::new failed")
        .into_raw()
}

/// # Safety
/// The ptr should be a valid pointer to the CString allocated by rust
#[unsafe(no_mangle)]
pub unsafe extern "C" fn free_sandwich_string(ptr: *const c_char) {
    let _ = unsafe { CString::from_raw(ptr as *mut _) };
}

/// Exercises the parts of the rust runtime that need more than libc: thread
/// spawning and unwinding across a caught panic. A C++ program linking this
/// staticlib has to pull in the corresponding system libraries, otherwise the
/// final link fails on undefined symbols.
///
/// Returns 0 when both the thread and the panic behaved as expected.
#[unsafe(no_mangle)]
pub extern "C" fn sandwich_runtime_check() -> i32 {
    let worker = std::thread::spawn(|| (1..=10).sum::<i32>());
    let sum = worker.join().expect("The worker thread never panics");

    let caught = std::panic::catch_unwind(|| -> i32 {
        panic!("panic on purpose to exercise unwinding");
    });

    if sum == 55 && caught.is_err() { 0 } else { 1 }
}
