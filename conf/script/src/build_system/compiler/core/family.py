from enum import Enum, unique

from ext.meta_prog.encapsulation import *


@export
@unique
class CompilerFamily(Enum):
    MSVC = 'msvc'
    CLANG = 'clang'
    GCC = 'gcc'
