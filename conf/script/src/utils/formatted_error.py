from typing import AnyStr

import colorama


def format_error_msg(error_msg: AnyStr) -> AnyStr:
    return colorama.Style.BRIGHT + colorama.Fore.RED + error_msg + colorama.Style.RESET_ALL


class FormattedError(BaseException):

    def __init__(self, error_msg: str, *args):
        super().__init__(format_error_msg(error_msg), *args)
