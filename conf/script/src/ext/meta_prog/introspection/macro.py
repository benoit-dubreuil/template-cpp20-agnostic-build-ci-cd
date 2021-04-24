__all__ = ['Macro']

from enum import Enum, auto, unique
from typing import Final, final


class _AutoMacroFromName(str, Enum):

    @final
    def _generate_next_value_(name: str, start, count, last_values, *args) -> (str, ...):
        __AFFIX: Final[str] = '__'
        return __AFFIX + name.lower() + __AFFIX, *args


@final
@unique
class Macro(_AutoMacroFromName):
    ALL = auto()
    DICT = auto()
    MAIN = auto()
    NAME = auto()
    QUALNAME = auto()


Macro.ALL.TAlias_Macro_All = list[str]
