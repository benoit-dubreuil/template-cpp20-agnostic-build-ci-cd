import argparse
from typing import Union

import utils.cli.error_meta
import utils.error.status
import utils.error.format


class SuccessWarning(UserWarning, utils.error.status.EncodedError, utils.error.format.FormattedSuccess, metaclass=utils.cli.error_meta.ErrorMeta):

    def __init__(self):
        super().__init__('Success')

    @staticmethod
    def get_error_status() -> utils.error.status.ErrorStatus:
        return utils.error.status.ErrorStatus.SUCCESS


class ArgParserError(RuntimeError, utils.error.status.EncodedError, utils.error.format.FormattedError, metaclass=utils.cli.error_meta.ErrorMeta):

    def __init__(self, arg_parser_exception: Union[argparse.ArgumentError, argparse.ArgumentTypeError]):
        error_msg = 'Argument parser error'
        arg_parser_error_msg = str(arg_parser_exception)

        if arg_parser_error_msg != str() and arg_parser_error_msg != str(None):
            error_msg += '\n'
            error_msg += arg_parser_error_msg

        super().__init__(error_msg)

    @staticmethod
    def get_error_status() -> utils.error.status.ErrorStatus:
        return utils.error.status.ErrorStatus.ARG_PARSER


class UnsupportedError(RuntimeError, utils.error.status.EncodedError, utils.error.format.FormattedError, metaclass=utils.cli.error_meta.ErrorMeta):

    def __init__(self):
        super().__init__('Unsupported error')

    @staticmethod
    def get_error_status() -> utils.error.status.ErrorStatus:
        return utils.error.status.ErrorStatus.UNSUPPORTED


class UnknownParsedArgError(TypeError, utils.error.status.EncodedError, utils.error.format.FormattedError, metaclass=utils.cli.error_meta.ErrorMeta):

    def __init__(self, unknown_parsed_args: list[str]):
        super().__init__(f"Unsupported argument '{unknown_parsed_args}'")

    @staticmethod
    def get_error_status() -> utils.error.status.ErrorStatus:
        return utils.error.status.ErrorStatus.UNKNOWN_PARSED_ARG


class EmptyParsedArgError(ValueError, utils.error.status.EncodedError, utils.error.format.FormattedError, metaclass=utils.cli.error_meta.ErrorMeta):

    def __init__(self, arg: str):
        super().__init__(f"'{arg}' argument must be followed by a path string")

    @staticmethod
    def get_error_status() -> utils.error.status.ErrorStatus:
        return utils.error.status.ErrorStatus.EMPTY_PARSED_ARG


class RootDirNotFoundError(FileNotFoundError, utils.error.status.EncodedError, utils.error.format.FormattedError, metaclass=utils.cli.error_meta.ErrorMeta):

    def __init__(self):
        super().__init__('Root directory not found')

    @staticmethod
    def get_error_status() -> utils.error.status.ErrorStatus:
        return utils.error.status.ErrorStatus.ROOT_DIR_NOT_FOUND


class BuildDirNotFoundError(FileNotFoundError, utils.error.status.EncodedError, utils.error.format.FormattedError, metaclass=utils.cli.error_meta.ErrorMeta):

    def __init__(self):
        super().__init__('Build directory not found')

    @staticmethod
    def get_error_status() -> utils.error.status.ErrorStatus:
        return utils.error.status.ErrorStatus.BUILD_DIR_NOT_FOUND
