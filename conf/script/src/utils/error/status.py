import abc
import enum

import utils.error.meta


@enum.unique
class ErrorStatus(enum.IntEnum):
    SUCCESS = 0
    UNSUPPORTED = 1
    ARG_PARSER = 2
    UNKNOWN_PARSED_ARG = enum.auto()
    EMPTY_PARSED_ARG = enum.auto()
    ROOT_DIR_NOT_FOUND = enum.auto()
    BUILD_DIR_NOT_FOUND = enum.auto()
    BUILD_DIR_NOT_DIR = enum.auto()
    COMPILER_NOT_FOUND = enum.auto()


class EncodedErrorMixin(metaclass=utils.error.meta.ErrorMeta):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @staticmethod
    @abc.abstractmethod
    def get_error_status() -> ErrorStatus:
        ...
