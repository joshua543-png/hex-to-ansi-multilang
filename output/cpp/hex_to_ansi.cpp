#include <iostream>
#include <sstream>
#include <iomanip>

std::string hex_to_ansi(const std::string& hex) {
    unsigned int r, g, b;
    sscanf(hex.c_str() + 1, "%02x%02x%02x", &r, &g, &b);
    std::ostringstream oss;
    oss << "\033[38;2;" << r << ";" << g << ";" << b << "m";
    return oss.str();
}

int main() {
    std::cout << hex_to_ansi("#FF4500") << "Orange text\033[0m" << std::endl;
    return 0;
}
