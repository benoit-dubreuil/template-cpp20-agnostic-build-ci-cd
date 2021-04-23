from enum import Enum, unique

from ext.meta_prog.encapsulation import *


@export
@unique
class CompilerSanitizer(Enum):
    NONE = 'none'
    ADDRESS = 'address'
    THREAD = 'thread'
    UNDEFINED = 'undefined'
    MEMORY = 'memory'
