from enum import Enum, unique


@unique
class CompilerReqsSectionScheme(Enum):
    OS = 'os'
    MAJOR = 'major'
    MINOR = 'minor'  # Optional
