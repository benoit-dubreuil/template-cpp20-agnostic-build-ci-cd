import utils.cli


class BuildDirNotFoundError(FileNotFoundError):

    def __init__(self):
        super().__init__(self._get_error_msg_build_not_found())

    @staticmethod
    def _get_error_msg_build_not_found() -> str:
        return utils.cli.format_error_msg('Build directory not found')
