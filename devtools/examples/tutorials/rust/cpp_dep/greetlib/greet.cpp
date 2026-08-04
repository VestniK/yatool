#include "greet.h"

#include <cstdlib>
#include <cstring>
#include <string>

extern "C" char* greet_cpp(const char* name) {
    // std::string is used on purpose: it drags in the C++ runtime, so the
    // example checks that rustc links more than just libc for a native peer.
    const std::string msg = std::string("Hello dear ") + name + " from C++!";
    char* const res = static_cast<char*>(std::malloc(msg.size() + 1));
    if (res != nullptr) {
        std::memcpy(res, msg.c_str(), msg.size() + 1);
    }
    return res;
}

extern "C" void free_cpp_string(char* msg) {
    std::free(msg);
}
