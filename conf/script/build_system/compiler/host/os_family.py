from enum import Enum, unique


@unique
class OSFamily(Enum):
    WINDOWS = 'windows'
    DARWIN = 'darwin'
    LINUX = 'linux'
