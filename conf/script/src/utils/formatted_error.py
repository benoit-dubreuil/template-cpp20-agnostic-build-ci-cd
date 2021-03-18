from typing import AnyStr

import colorama


def format_error_msg(error_msg: AnyStr) -> AnyStr:
    return colorama.Style.BRIGHT + colorama.Fore.RED + error_msg + colorama.Style.RESET_ALL


class FormattedError(BaseException):

    def __init__(self, *args):
        formatted_args = [format_error_msg(arg) if isinstance(arg, str) else arg for arg in args]
        super().__init__(*formatted_args)
