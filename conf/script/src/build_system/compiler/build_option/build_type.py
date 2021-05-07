__all__ = ['TargetBuildType']

from enum import Enum, unique


@unique
class TargetBuildType(str, Enum):
    DEBUG = 'debug'
    DEBUG_OPTIMIZED = 'debugoptimized'
    RELEASE = 'release'
