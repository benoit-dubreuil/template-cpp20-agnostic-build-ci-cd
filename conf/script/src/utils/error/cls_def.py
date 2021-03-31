import argparse
from typing import Optional, Union

import utils.error.format
import utils.error.managed
import utils.error.status


@utils.error.managed.ManageClass(error_formatter_cls=utils.error.format.FormattedSuccessMixin, encoded_error_status=utils.error.status.ErrorStatus.SUCCESS)
class SuccessWarning(UserWarning):

    def __init__(self):
        super().__init__('Success')


@utils.error.managed.ManageClass(encoded_error_status=utils.error.status.ErrorStatus.UNSUPPORTED)
class UnsupportedError(RuntimeError):

    def __init__(self, original_raised_error: Optional[BaseException] = None):
        error_msg = 'Unsupported error'

        if original_raised_error is not None:
            error_msg += '\n'
            error_msg += str(original_raised_error)

        super().__init__('Unsupported error')

        if original_raised_error is not None:
            self.with_traceback(original_raised_error.__traceback__)


@utils.error.managed.ManageClass(encoded_error_status=utils.error.status.ErrorStatus.ARG_PARSER)
class ArgParserError(RuntimeError):

    def __init__(self, arg_parser_exception: Union[argparse.ArgumentError, argparse.ArgumentTypeError]):
        error_msg = 'Argument parser error'
        arg_parser_error_msg = str(arg_parser_exception)

        if arg_parser_error_msg != str() and arg_parser_error_msg != str(None):
            error_msg += '\n'
            error_msg += arg_parser_error_msg

        super().__init__(error_msg)


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


@utils.error.managed.ManageClass(encoded_error_status=utils.error.status.ErrorStatus.BUILD_DIR_NOT_DIR)
class BuildDirNotDirError(FileExistsError):

    def __init__(self):
        super().__init__("Build directory exists but isn't a directory")


@utils.error.managed.ManageClass(encoded_error_status=utils.error.status.ErrorStatus.BUILD_DIR_NOT_EMPTY)
class BuildDirNotEmptyError(FileExistsError):

    def __init__(self):
        super().__init__("Build directory isn't empty")


@utils.error.managed.ManageClass(encoded_error_status=utils.error.status.ErrorStatus.CONF_DIR_NOT_FOUND)
class ConfDirNotFoundError(FileNotFoundError):

    def __init__(self):
        super().__init__('Conf directory not found')


@utils.error.managed.ManageClass(encoded_error_status=utils.error.status.ErrorStatus.COMPILER_NOT_FOUND)
class CompilerNotFoundError(FileNotFoundError):

    def __init__(self, error_msg: str = 'Compiler at the supplied path does not exist or requires ungranted permissions'):
        super().__init__(error_msg)


class NoSupportedCompilersAvailableError(CompilerNotFoundError):

    def __init__(self):
        super().__init__(error_msg='No supported compilers are available')

    @staticmethod
    def get_error_status() -> utils.error.status.ErrorStatus:
        return utils.error.status.ErrorStatus.NO_SUPPORTED_COMPILERS_AVAILABLE


@utils.error.managed.ManageClass(encoded_error_status=utils.error.status.ErrorStatus.MSVC_COMPILER_VCVARS_DIR_NOT_FOUND)
class MSVCCompilerVcvarsDirNotFoundError(FileNotFoundError):

    def __init__(self):
        super().__init__('MSVC compiler vcvars directory not found')


@utils.error.managed.ManageClass(encoded_error_status=utils.error.status.ErrorStatus.MSVC_COMPILER_VCVARS_BATCH_FILE_NOT_FOUND)
class MSVCCompilerVcvarsBatchFileNotFoundError(FileNotFoundError):

    def __init__(self):
        super().__init__('MSVC compiler vcvars batch file for supported architecture not found')
