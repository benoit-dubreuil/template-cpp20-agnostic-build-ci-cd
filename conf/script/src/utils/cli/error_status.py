import abc
import enum


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
