import argparse
from typing import Union

import utils.error.format
import utils.error.managed
import utils.error.status


@utils.error.managed.ManageClass(error_formatter_cls=utils.error.format.FormattedSuccess, encoded_error_status=utils.error.status.ErrorStatus.SUCCESS)
class SuccessWarning(UserWarning):

    def __init__(self):
        super().__init__('Success')


@utils.error.managed.ManageClass(encoded_error_status=utils.error.status.ErrorStatus.ARG_PARSER)
class ArgParserError(RuntimeError):

    def __init__(self, arg_parser_exception: Union[argparse.ArgumentError, argparse.ArgumentTypeError]):
        error_msg = 'Argument parser error'
        arg_parser_error_msg = str(arg_parser_exception)

        if arg_parser_error_msg != str() and arg_parser_error_msg != str(None):
            error_msg += '\n'
            error_msg += arg_parser_error_msg

        super().__init__(error_msg)


@utils.error.managed.ManageClass(encoded_error_status=utils.error.status.ErrorStatus.UNSUPPORTED)
class UnsupportedError(RuntimeError):

    def __init__(self):
        super().__init__('Unsupported error')


@utils.error.managed.ManageClass(encoded_error_status=utils.error.status.ErrorStatus.UNKNOWN_PARSED_ARG)
class UnknownParsedArgError(TypeError):

    def __init__(self, unknown_parsed_args: list[str]):
        super().__init__(f"Unsupported argument '{unknown_parsed_args}'")


@utils.error.managed.ManageClass(encoded_error_status=utils.error.status.ErrorStatus.EMPTY_PARSED_ARG)
class EmptyParsedArgError(ValueError):

    def __init__(self, arg: str):
        super().__init__(f"'{arg}' argument must be followed by a path string")


@utils.error.managed.ManageClass(encoded_error_status=utils.error.status.ErrorStatus.ROOT_DIR_NOT_FOUND)
class RootDirNotFoundError(FileNotFoundError):

    def __init__(self):
        super().__init__('Root directory not found')


@utils.error.managed.ManageClass(encoded_error_status=utils.error.status.ErrorStatus.BUILD_DIR_NOT_FOUND)
class BuildDirNotFoundError(FileNotFoundError):

    def __init__(self):
        super().__init__('Build directory not found')


@utils.error.managed.ManageClass(encoded_error_status=utils.error.status.ErrorStatus.COMPILER_NOT_FOUND)
class CompilerNotFoundError(FileNotFoundError):

    def __init__(self):
        super().__init__('Compiler at the supplied path does not exist or requires ungranted permissions')
