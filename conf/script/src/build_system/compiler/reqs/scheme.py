__all__ = ['CompilerReqsScheme']

from enum import Enum, unique


@unique
class CompilerReqsScheme(str, Enum):
    OS = 'os'
    MAJOR = 'major'
    MINOR = 'minor'  # Optional
