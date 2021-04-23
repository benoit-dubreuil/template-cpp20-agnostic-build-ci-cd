import platform
from enum import Enum, unique


@unique
class OSFamily(Enum):
    WINDOWS = 'windows'
    DARWIN = 'darwin'
    LINUX = 'linux'

    @classmethod
    def detect(cls) -> 'OSFamily':
        os_name: str = cls.fetch_os_name()
        return cls(os_name)

    @staticmethod
    def fetch_os_name() -> str:
        return platform.system().lower()
