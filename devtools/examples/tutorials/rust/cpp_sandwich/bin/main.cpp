#include <iostream>
#include <memory>

extern "C" const char* sandwich_greet(const char*);
extern "C" void free_sandwich_string(const char*) noexcept;
extern "C" int sandwich_runtime_check();

namespace {

    struct sandwich_str_delete {
        void operator()(const char* p) const noexcept {
            free_sandwich_string(p);
        }
    };
    using sandwich_str_ptr = std::unique_ptr<const char, sandwich_str_delete>;

}

int main() {
    // C++ -> rust -> C++: the greeting is produced by greetlib, wrapped by the
    // rust staticlib and printed here. It only links if greetlib reaches this
    // final link through the rust module in between.
    sandwich_str_ptr msg{sandwich_greet("World")};
    std::cout << msg.get() << "\n";

    // Threads and unwinding need more of the rust runtime than plain libc.
    if (sandwich_runtime_check() != 0) {
        std::cerr << "rust runtime check failed\n";
        return 1;
    }
    std::cout << "rust runtime check passed\n";
    return 0;
}
