from enum import Enum, IntFlag, unique


@unique
class Architecture(IntFlag):
    UNKNOWN = 0
    A_16 = 2 ** 4
    A_32 = 2 ** 5
    A_64 = 2 ** 6
    A_128 = 2 ** 7

    def arch_to_bit_name(self) -> str:
        return str(self.value) + 'bit'


@unique
class BuildType(Enum):
    DEBUG = 'debug'
    DEBUG_OPTIMIZED = 'debugoptimized'
    RELEASE = 'release'


@unique
class CompilerReqsSectionScheme(Enum):
    OS = 'os'
    MAJOR = 'major'
    MINOR = 'minor'  # Optional
