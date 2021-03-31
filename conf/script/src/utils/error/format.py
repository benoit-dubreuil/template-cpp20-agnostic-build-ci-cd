import abc
from typing import AnyStr

import colorama

import utils.error.meta


def format_error_msg(message: AnyStr) -> AnyStr:
    return colorama.Style.BRIGHT + colorama.Fore.RED + message + colorama.Style.RESET_ALL


def format_success_msg(message: AnyStr) -> AnyStr:
    return colorama.Style.BRIGHT + colorama.Fore.GREEN + message + colorama.Style.RESET_ALL


class BaseFormattedErrorMixin(Exception, metaclass=utils.error.meta.ErrorMeta):

    def __init__(self, *args, **kwargs):
        # noinspection PyArgumentList
        super().__init__(*args, **kwargs)

    def __str__(self) -> str:
        error_msg = super().__str__()
        return self._format_msg(error_msg)

    @staticmethod
    @abc.abstractmethod
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
