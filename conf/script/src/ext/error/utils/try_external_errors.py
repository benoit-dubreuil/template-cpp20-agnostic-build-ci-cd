__all__ = ['try_manage_external_errors',
           'try_manage_strict_path_resolving']

from pathlib import Path
from typing import Callable, TypeVar

from ..core import *

_T_Exception: TypeVar = TypeVar('_T_Exception', bound=Exception)
_T_ManagedException: TypeVar = TypeVar('_T_ManagedException', bound=Exception)

_TAlias_external_errors_to_manage = {tuple[type[_T_Exception], ...]: type[_T_ManagedException]}

_DEFAULT_EXTERNAL_ERRORS_TO_MANAGE: _TAlias_external_errors_to_manage = {(Exception,): UnsupportedError}


def try_manage_external_errors(func_to_try: Callable,
                               external_errors_to_manage: _TAlias_external_errors_to_manage = None):
    assert func_to_try is not None

    if external_errors_to_manage is None:
        external_errors_to_manage = _DEFAULT_EXTERNAL_ERRORS_TO_MANAGE

    assert len(external_errors_to_manage) > 0

    try:
        func_to_try()

    except Exception as raised_error:

        supported_external_error_types: tuple[type[Exception]]
        managed_error_type: type[UnsupportedError]

        for supported_external_error_types, managed_error_type in external_errors_to_manage.items():
            for external_error_type in supported_external_error_types:
                if isinstance(raised_error, external_error_type):
                    managed_error = managed_error_type()
                    managed_error.with_traceback(raised_error.__traceback__)

                    raise managed_error

        raise raised_error


def try_manage_strict_path_resolving(path_to_resolve: Path,
                                     external_errors_to_manage: _TAlias_external_errors_to_manage = None):
    try_manage_external_errors(func_to_try=lambda: path_to_resolve.resolve(strict=True),
                               external_errors_to_manage=external_errors_to_manage)
