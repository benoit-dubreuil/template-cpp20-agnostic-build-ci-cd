from enum import Enum, unique

from ext.meta_prog.encapsulation import *


@export
@unique
class CompilerReqsScheme(Enum):
    OS = 'os'
    MAJOR = 'major'
    MINOR = 'minor'  # Optional
