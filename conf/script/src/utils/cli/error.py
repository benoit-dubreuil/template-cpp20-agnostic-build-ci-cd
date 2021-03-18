import enum

import utils.formatted_error


class ErrorStatus(enum.IntEnum):
    UNSUPPORTED_ERROR = 1
    ARG_PARSER_DEFAULT = 2
    UNKNOWN_PARSED_ARG = enum.auto()
    EMPTY_PARSED_ARG = enum.auto()
    ROOT_DIR_NOT_FOUND = enum.auto()
    BUILD_DIR_NOT_FOUND = enum.auto()


class UnknownParsedArgError(TypeError, utils.formatted_error.FormattedError):

    def __init__(self, unknown_parsed_args: list[str]):
        super().__init__(f"Unsupported argument '{unknown_parsed_args}'")


class EmptyParsedArgError(ValueError, utils.formatted_error.FormattedError):

    def __init__(self, arg: str):
        super().__init__(f"'{arg}' argument must be followed by a path string")


class RootDirNotFoundError(FileNotFoundError, utils.formatted_error.FormattedError):

    def __init__(self):
        super().__init__(f'Root directory not found')


class BuildDirNotFoundError(FileNotFoundError):

    def __init__(self):
        super().__init__(f'Build directory not found')
