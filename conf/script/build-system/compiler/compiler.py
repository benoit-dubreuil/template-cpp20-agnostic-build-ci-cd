from enum import unique, Enum


@unique
class Compiler(Enum):
    MSVC = 'msvc'
    CLANG = 'clang'
    GCC = 'gcc'
