import utils.formatted_error


class RootDirNotFoundError(FileNotFoundError):

    def __init__(self):
        super().__init__(self._get_error_msg_root_not_found())

    @staticmethod
    def _get_error_msg_root_not_found() -> str:
        return utils.formatted_error.format_exception_msg('Root directory not found')
