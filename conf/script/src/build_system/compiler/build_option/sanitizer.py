__all__ = ['CompilerSanitizer']

from enum import Enum, unique


@unique
class CompilerSanitizer(str, Enum):
    NONE = 'none'
    ADDRESS = 'address'
    THREAD = 'thread'
    UNDEFINED = 'undefined'
    MEMORY = 'memory'
