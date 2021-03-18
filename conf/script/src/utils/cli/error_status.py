import abc
import enum

import utils.cli.error_meta


@enum.unique
class ErrorStatus(enum.IntEnum):
    SUCCESS = 0
    UNSUPPORTED = 1
    ARG_PARSER = 2
    UNKNOWN_PARSED_ARG = enum.auto()
    EMPTY_PARSED_ARG = enum.auto()
    ROOT_DIR_NOT_FOUND = enum.auto()
    BUILD_DIR_NOT_FOUND = enum.auto()


class EncodedError(Exception, abc.ABC, metaclass=utils.cli.error_meta.ErrorMeta):

    @staticmethod
    @abc.abstractmethod
    def get_error_status() -> ErrorStatus:
        ...
