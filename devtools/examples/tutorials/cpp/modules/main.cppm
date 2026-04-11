module;

#include <iostream>

export module main;

import greet;

int main() {
  std::cout << make_greet("World") << '\n';
  return 0;
}
