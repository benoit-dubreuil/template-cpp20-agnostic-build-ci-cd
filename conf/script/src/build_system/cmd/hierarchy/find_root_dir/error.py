import utils.cli


class RootDirNotFoundError(FileNotFoundError):

    def __init__(self):
        super().__init__(self._get_error_msg_root_not_found())

    @staticmethod
    def _get_error_msg_root_not_found() -> str:
        return utils.cli.format_error_msg('Root directory not found')
