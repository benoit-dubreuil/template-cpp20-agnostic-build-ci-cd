from enum import Enum, unique

from ext.meta_prog.encapsulation import *


@export
@unique
class TargetBuildType(Enum):
    DEBUG = 'debug'
    DEBUG_OPTIMIZED = 'debugoptimized'
    RELEASE = 'release'
