module;

#include <format>

export module greet;

export std::string make_greet(const std::string& name) {
    return std::format("Hello {}", name);
}
