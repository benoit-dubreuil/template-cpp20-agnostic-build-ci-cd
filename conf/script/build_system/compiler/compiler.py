from enum import Enum, unique


@unique
class Compiler(Enum):
    MSVC = 'msvc'
    CLANG = 'clang'
    GCC = 'gcc'
