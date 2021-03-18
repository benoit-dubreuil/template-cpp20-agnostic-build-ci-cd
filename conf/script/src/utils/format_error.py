from typing import AnyStr

import colorama


def format_error_msg(message: AnyStr) -> AnyStr:
    return colorama.Style.BRIGHT + colorama.Fore.RED + message + colorama.Style.RESET_ALL


def format_success_msg(message: AnyStr) -> AnyStr:
    return colorama.Style.BRIGHT + colorama.Fore.GREEN + message + colorama.Style.RESET_ALL


class FormattedError(BaseException):

    def __init__(self, message: str, *args):
        super().__init__(format_error_msg(message), *args)


class FormattedSuccess(BaseException):

    def __init__(self, message: str, *args):
        super().__init__(format_success_msg(message), *args)
