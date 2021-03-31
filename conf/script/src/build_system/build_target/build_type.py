from enum import Enum, unique


@unique
class TargetBuildType(Enum):
    DEBUG = 'debug'
    DEBUG_OPTIMIZED = 'debugoptimized'
    RELEASE = 'release'
