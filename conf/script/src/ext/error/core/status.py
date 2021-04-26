__all__ = ['ErrorStatus',
           'EncodedErrorMixin']

from abc import abstractmethod
from enum import IntEnum, auto, unique

from .meta import *


@unique
class ErrorStatus(IntEnum):
    SUCCESS = 0
    UNSUPPORTED = 1

    ARG_PARSER = 2

    UNKNOWN_PARSED_ARG = auto()
    EMPTY_PARSED_ARG = auto()

    ROOT_DIR_NOT_FOUND = auto()
    ROOT_DIR_NOT_DIR = auto()
    BUILD_DIR_NOT_FOUND = auto()
    BUILD_DIR_NOT_DIR = auto()
    BUILD_DIR_NOT_EMPTY = auto()

    CONF_DIR_NOT_FOUND = auto()
    CONF_BUILD_SYSTEM_DIR_NOT_FOUND = auto()

    MESON_MAIN_FILE_NOT_FOUND = auto()
    MESON_MACHINE_FILES_DIR_NOT_FOUND = auto()

    COMPILER_REQS_NOT_FOUND = auto()
    COMPILER_NOT_FOUND = auto()
    NO_SUPPORTED_COMPILERS_AVAILABLE = auto()

    MSVC_COMPILER_VCVARS_DIR_NOT_FOUND = auto()
    MSVC_COMPILER_VCVARS_BATCH_FILE_NOT_FOUND = auto()


class EncodedErrorMixin(Exception, metaclass=ErrorMeta):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @staticmethod
    @abstractmethod
    def get_error_status() -> ErrorStatus:
        raise NotImplementedError()
