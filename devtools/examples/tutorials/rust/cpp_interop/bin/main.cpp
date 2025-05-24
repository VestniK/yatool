#include "rs_str_ptr.h"

#include <iostream>

extern "C" const char* greet_rs(const char*);

int main() {
    rs_str_ptr msg{greet_rs("World")};
    std::cout << msg.get() << "\n";
    return 0;
}
