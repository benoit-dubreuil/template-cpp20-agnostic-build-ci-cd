import abc
import enum

import utils.error.error_meta


@enum.unique
class ErrorStatus(enum.IntEnum):
    SUCCESS = 0
    UNSUPPORTED = 1
    ARG_PARSER = 2
    UNKNOWN_PARSED_ARG = enum.auto()
    EMPTY_PARSED_ARG = enum.auto()
    ROOT_DIR_NOT_FOUND = enum.auto()
    BUILD_DIR_NOT_FOUND = enum.auto()


class EncodedError(abc.ABC, Exception, metaclass=utils.error.error_meta.ErrorMeta):

    @staticmethod
    @abc.abstractmethod
    def get_error_status() -> ErrorStatus:
        ...
