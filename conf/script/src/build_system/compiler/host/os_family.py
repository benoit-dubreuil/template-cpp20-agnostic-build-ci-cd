import platform
from enum import Enum, unique


@unique
class OSFamily(Enum):
    WINDOWS = 'windows'
    DARWIN = 'darwin'
    LINUX = 'linux'


def fetch_os_name() -> str:
    return platform.system().lower()


def fetch_os_family() -> OSFamily:
    return OSFamily(fetch_os_name())
