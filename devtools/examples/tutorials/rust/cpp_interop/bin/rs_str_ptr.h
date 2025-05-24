#include <memory>

extern "C" void free_rs_string(const char*) noexcept;

struct rs_str_delete {
    void operator() (const char* p) const noexcept {
        free_rs_string(p);
    }
};
using rs_str_ptr = std::unique_ptr<const char, rs_str_delete>;
