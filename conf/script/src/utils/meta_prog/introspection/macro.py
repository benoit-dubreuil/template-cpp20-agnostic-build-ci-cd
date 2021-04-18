from enum import Enum, auto, unique
from typing import Final


@unique
class AutoMacroFromName(Enum):
    __AFFIX: Final[str] = '__'

    def _generate_next_value_(name: str, start, count, last_values) -> str:
        affixed_name = AutoMacroFromName.__AFFIX + name + AutoMacroFromName.__AFFIX
        return affixed_name


@unique
class Macro(AutoMacroFromName):
    ALL = auto()
    NAME = auto()
    QUALNAME = auto()
