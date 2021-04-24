__all__ = ['CompilerFamily']

from enum import Enum, unique


@unique
class CompilerFamily(Enum):
    MSVC = 'msvc'
    CLANG = 'clang'
    GCC = 'gcc'
