import abc
import enum

import utils.error.meta
from utils.meta_prog.encapsulation import *


@enum.unique
@export
class ErrorStatus(enum.IntEnum):
    SUCCESS = 0
    UNSUPPORTED = 1

    ARG_PARSER = 2

    UNKNOWN_PARSED_ARG = enum.auto()
    EMPTY_PARSED_ARG = enum.auto()

    ROOT_DIR_NOT_FOUND = enum.auto()
    BUILD_DIR_NOT_FOUND = enum.auto()
    BUILD_DIR_NOT_DIR = enum.auto()
    BUILD_DIR_NOT_EMPTY = enum.auto()

    CONF_DIR_NOT_FOUND = enum.auto()
    CONF_BUILD_SYSTEM_DIR_NOT_FOUND = enum.auto()

    MESON_MAIN_FILE_NOT_FOUND = enum.auto()
    MESON_MACHINE_FILES_DIR_NOT_FOUND = enum.auto()

    COMPILER_REQS_NOT_FOUND = enum.auto()
    COMPILER_NOT_FOUND = enum.auto()
    NO_SUPPORTED_COMPILERS_AVAILABLE = enum.auto()

    MSVC_COMPILER_VCVARS_DIR_NOT_FOUND = enum.auto()
    MSVC_COMPILER_VCVARS_BATCH_FILE_NOT_FOUND = enum.auto()


@export
class EncodedErrorMixin(Exception, metaclass=utils.error.meta.ErrorMeta):

    def __init__(self, *args, **kwargs):
        # noinspection PyArgumentList
        super().__init__(*args, **kwargs)

    @staticmethod
    @abc.abstractmethod
    def get_error_status() -> ErrorStatus:
        raise NotImplementedError()
