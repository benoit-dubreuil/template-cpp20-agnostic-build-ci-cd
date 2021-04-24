__all__ = ['Macro', 'TAlias_Macro_All']

from enum import Enum, auto, unique
from typing import Any, Final, final

TAlias_Macro_All = list[str]


class _AutoMacroFromName(str, Enum):

    @final
    def _generate_next_value_(name: str, start, count, last_values, *args) -> (str, ...):
        __AFFIX: Final[str] = '__'
        return __AFFIX + name.lower() + __AFFIX, *args


@final
@unique
class Macro(_AutoMacroFromName):
    ALL = auto(('TAlias_Macro_All', list[str]))
    DICT = auto()
    MAIN = auto()
    NAME = auto()
    QUALNAME = auto()

    def __new__(cls, value, *args: tuple[str, Any]):
        macro = str().__new__(cls, value)

        for attr_name, attr_val in args:
            setattr(macro, attr_name, attr_val)

        return macro
