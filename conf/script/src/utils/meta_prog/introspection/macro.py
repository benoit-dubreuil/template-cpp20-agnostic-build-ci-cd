from enum import Enum, auto, unique
from typing import Final

TAlias_Macro_All = list[str]

__all__ = ['Macro', 'TAlias_Macro_All']


class AutoMacroFromName(str, Enum):

    def _generate_next_value_(name: str, start, count, last_values) -> str:
        __AFFIX: Final[str] = '__'
        return __AFFIX + name.lower() + __AFFIX


@unique
class Macro(AutoMacroFromName):
    ALL = auto()
    DICT = auto()
    MAIN = auto()
    NAME = auto()
    QUALNAME = auto()
