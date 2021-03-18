import abc
import enum

import utils.formatted_error


class ErrorStatus(enum.IntEnum):
    UNSUPPORTED_ERROR = 1
    ARG_PARSER_DEFAULT = 2
    UNKNOWN_PARSED_ARG = enum.auto()
    EMPTY_PARSED_ARG = enum.auto()
    ROOT_DIR_NOT_FOUND = enum.auto()
    BUILD_DIR_NOT_FOUND = enum.auto()


class EncodedErrorMeta(abc.ABCMeta, type):
    pass


class EncodedError(BaseException, abc.ABC, metaclass=EncodedErrorMeta):

    @staticmethod
    @abc.abstractmethod
    def get_error_status():
        ...


class UnknownParsedArgError(TypeError, EncodedError, utils.formatted_error.FormattedError, metaclass=EncodedErrorMeta):

    def __init__(self, unknown_parsed_args: list[str]):
        super().__init__(f"Unsupported argument '{unknown_parsed_args}'")

    @staticmethod
    def get_error_status():
        return ErrorStatus.UNKNOWN_PARSED_ARG


class EmptyParsedArgError(ValueError, EncodedError, utils.formatted_error.FormattedError, metaclass=EncodedErrorMeta):

    def __init__(self, arg: str):
        super().__init__(f"'{arg}' argument must be followed by a path string")

    @staticmethod
    def get_error_status():
        return ErrorStatus.EMPTY_PARSED_ARG


class RootDirNotFoundError(FileNotFoundError, EncodedError, utils.formatted_error.FormattedError, metaclass=EncodedErrorMeta):

    def __init__(self):
        super().__init__(f'Root directory not found')

    @staticmethod
    def get_error_status():
        return ErrorStatus.ROOT_DIR_NOT_FOUND


class BuildDirNotFoundError(FileNotFoundError, EncodedError, utils.formatted_error.FormattedError, metaclass=EncodedErrorMeta):

    def __init__(self):
        super().__init__(f'Build directory not found')

    @staticmethod
    def get_error_status():
        return ErrorStatus.BUILD_DIR_NOT_FOUND
