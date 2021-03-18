import abc
from typing import AnyStr

import colorama

import utils.cli.error_meta


def format_error_msg(message: AnyStr) -> AnyStr:
    return colorama.Style.BRIGHT + colorama.Fore.RED + message + colorama.Style.RESET_ALL


def format_success_msg(message: AnyStr) -> AnyStr:
    return colorama.Style.BRIGHT + colorama.Fore.GREEN + message + colorama.Style.RESET_ALL


class BaseFormattedError(Exception, abc.ABC, metaclass=utils.cli.error_meta.ManagedErrorMeta):

    def __init__(self, message: str, *args):
        super().__init__(self._format_msg(message), *args)

    @staticmethod
    @abc.abstractmethod
    def _format_msg(message: str) -> str:
        ...


class FormattedError(BaseFormattedError):

    @staticmethod
    def _format_msg(message: str) -> str:
        return format_error_msg(message)


class FormattedSuccess(BaseFormattedError):

    @staticmethod
    def _format_msg(message: str) -> str:
        return format_success_msg(message)