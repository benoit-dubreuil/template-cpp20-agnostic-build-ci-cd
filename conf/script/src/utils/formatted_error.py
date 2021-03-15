#!/usr/bin/env python3

from abc import ABC
from typing import AnyStr

import colorama


def format_exception_msg(error_msg: AnyStr) -> AnyStr:
    return colorama.Style.BRIGHT + colorama.Fore.RED + error_msg + colorama.Style.RESET_ALL


class FormattedException(BaseException):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, kwargs)
