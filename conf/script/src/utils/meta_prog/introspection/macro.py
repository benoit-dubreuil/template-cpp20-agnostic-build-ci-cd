from enum import Enum, auto, unique
from typing import Final

TAlias_Macro_All = list[str]

__all__: TAlias_Macro_All = ['Macro']


@unique
class AutoMacroFromName(str, Enum):
    __AFFIX: Final[str] = '__'

    def _generate_next_value_(name: str, start, count, last_values) -> str:
        affixed_name = AutoMacroFromName.__AFFIX + name + AutoMacroFromName.__AFFIX
        return affixed_name


@unique
class Macro(AutoMacroFromName):
    ALL = auto()
    MAIN = auto()
    NAME = auto()
    QUALNAME = auto()
