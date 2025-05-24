use std::ffi::{CStr, CString};
use std::io::Write;
use std::os::raw::c_char;

#[unsafe(no_mangle)]
pub unsafe extern "C" fn greet_rs(name: *const c_char) -> *const c_char {
    let name = unsafe { CStr::from_ptr(name) };
    let name = name.to_str().expect("The message is always valid UTF8");

    let mut res_data = Vec::<u8>::default();
    write!(&mut res_data, "Hello dear {}!", name).expect("Failed to write greeting message");
    CString::new(res_data)
        .expect("CString::new failed")
        .into_raw()
}

/// # Safety
/// The ptr should be a valid pointer to the CString allocated by rust
#[unsafe(no_mangle)]
pub unsafe extern "C" fn free_rs_string(ptr: *const c_char) {
    let _ = unsafe { CString::from_raw(ptr as *mut _) };
}
