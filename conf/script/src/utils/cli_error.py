import enum
from enum import IntEnum


class ErrorStatus(IntEnum):
    ARG_PARSER_DEFAULT = 2
    UNKNOWN_PARSED_ARG = enum.auto()
    EMPTY_PARSED_ARG = enum.auto()

