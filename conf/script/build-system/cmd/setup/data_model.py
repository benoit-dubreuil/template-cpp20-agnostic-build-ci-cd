from enum import Enum, unique


@unique
class BuildType(Enum):
    DEBUG = 'debug'
    DEBUG_OPTIMIZED = 'debugoptimized'
    RELEASE = 'release'
