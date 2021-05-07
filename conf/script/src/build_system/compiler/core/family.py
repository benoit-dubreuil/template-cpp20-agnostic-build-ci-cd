__all__ = ['CompilerFamily']

from enum import Enum, unique


@unique
class CompilerFamily(str, Enum):
    MSVC = 'msvc'
    CLANG = 'clang'
    GCC = 'gcc'
