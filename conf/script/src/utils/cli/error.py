import utils.cli.error_status
import utils.format_error
import utils.cli.error_meta

from utils.cli.error_status import EncodedError


class SuccessWarning(UserWarning, EncodedError, utils.format_error.FormattedSuccess, metaclass=utils.cli.error_meta.ManagedErrorMeta):

    def __init__(self):
        super().__init__('Success')

    @staticmethod
    def get_error_status():
        return utils.cli.error_status.ErrorStatus.SUCCESS


class UnsupportedError(RuntimeError, EncodedError, utils.format_error.FormattedError, metaclass=utils.cli.error_meta.ManagedErrorMeta):

    def __init__(self):
        super().__init__('Unsupported error')

    @staticmethod
    def get_error_status():
        return utils.cli.error_status.ErrorStatus.UNSUPPORTED


class UnknownParsedArgError(TypeError, EncodedError, utils.format_error.FormattedError, metaclass=utils.cli.error_meta.ManagedErrorMeta):

    def __init__(self, unknown_parsed_args: list[str]):
        super().__init__(f"Unsupported argument '{unknown_parsed_args}'")

    @staticmethod
    def get_error_status():
        return utils.cli.error_status.ErrorStatus.UNKNOWN_PARSED_ARG


class EmptyParsedArgError(ValueError, EncodedError, utils.format_error.FormattedError, metaclass=utils.cli.error_meta.ManagedErrorMeta):

    def __init__(self, arg: str):
        super().__init__(f"'{arg}' argument must be followed by a path string")

    @staticmethod
    def get_error_status():
        return utils.cli.error_status.ErrorStatus.EMPTY_PARSED_ARG


class RootDirNotFoundError(FileNotFoundError, EncodedError, utils.format_error.FormattedError, metaclass=utils.cli.error_meta.ManagedErrorMeta):

    def __init__(self):
        super().__init__('Root directory not found')

    @staticmethod
    def get_error_status():
        return utils.cli.error_status.ErrorStatus.ROOT_DIR_NOT_FOUND


class BuildDirNotFoundError(FileNotFoundError, EncodedError, utils.format_error.FormattedError, metaclass=utils.cli.error_meta.ManagedErrorMeta):

    def __init__(self):
        super().__init__('Build directory not found')

    @staticmethod
    def get_error_status():
        return utils.cli.error_status.ErrorStatus.BUILD_DIR_NOT_FOUND
