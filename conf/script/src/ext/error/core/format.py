__all__ = ['format_error_msg',
           'format_success_msg',
           'BaseFormattedErrorMixin',
           'FormattedErrorMixin',
           'FormattedSuccessMixin']

from abc import abstractmethod
from typing import AnyStr

import colorama

from .meta import *


def format_error_msg(message: AnyStr) -> AnyStr:
    return colorama.Style.BRIGHT + colorama.Fore.RED + message + colorama.Style.RESET_ALL


def format_success_msg(message: AnyStr) -> AnyStr:
    return colorama.Style.BRIGHT + colorama.Fore.GREEN + message + colorama.Style.RESET_ALL


class BaseFormattedErrorMixin(Exception, metaclass=ErrorMeta):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __str__(self) -> str:
        error_msg = super().__str__()
        return self._format_msg(error_msg)

    @staticmethod
    @abstractmethod
    def _format_msg(message: str) -> str:
        raise NotImplementedError()


class FormattedErrorMixin(BaseFormattedErrorMixin):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @staticmethod
    def _format_msg(message: str) -> str:
        return format_error_msg(message)


class FormattedSuccessMixin(BaseFormattedErrorMixin):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @staticmethod
    def _format_msg(message: str) -> str:
        return format_success_msg(message)
