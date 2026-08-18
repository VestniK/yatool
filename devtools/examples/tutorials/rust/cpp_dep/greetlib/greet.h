#pragma once

extern "C" {

// Returns a NUL-terminated greeting allocated with malloc().
// The caller owns the result and must release it with free_cpp_string().
char* greet_cpp(const char* name);

void free_cpp_string(char* msg);

}
