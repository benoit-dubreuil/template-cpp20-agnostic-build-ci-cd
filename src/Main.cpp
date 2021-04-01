import std.core;

int main() {
    constexpr char space[] = "   ";
    std::cout << "Hello World!" << std::endl;

#ifdef __STDC_VERSION__
    std::cout << "C version:" << space << __STDC_VERSION__ << std::endl;
#endif

#ifdef __cplusplus
    std::cout << "C++ version:" << space << __cplusplus << std::endl;
#endif

#ifdef _MSC_VER
    std::cout << "Visual Studio:" << space;

    std::cout << "_MSC_VER:" << space << _MSC_VER << space;
    std::cout << "_MSC_FULL_VER:" << space << _MSC_FULL_VER;

    std::cout << std::endl;
#endif

    return 0;
}
