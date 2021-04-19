from pathlib import Path
from typing import Callable, Type

from .cls_def import *
from .managed import *
from utils.error.cls_def import UnsupportedError
from utils.meta_prog.encapsulation import *


@export
def try_manage_external_errors(func_to_try: Callable,
                               external_errors_to_manage: {tuple[Type[Exception], ...]: Type[ManagedErrorMixin]} = {
                                   (Exception,): UnsupportedError}):
    assert func_to_try is not None
    assert external_errors_to_manage is not None
    assert len(external_errors_to_manage) > 0

    try:
        func_to_try()

    except Exception as raised_error:

        supported_external_error_types: tuple[Type[Exception]]
        managed_error_type: Type[UnsupportedError]

        for supported_external_error_types, managed_error_type in external_errors_to_manage.items():
            for external_error_type in supported_external_error_types:
                if isinstance(raised_error, external_error_type):
                    managed_error = managed_error_type()
                    managed_error.with_traceback(raised_error.__traceback__)

                    raise managed_error

        raise raised_error


@export
def try_manage_strict_path_resolving(path_to_resolve: Path,
                                     external_errors_to_manage: {tuple[Type[Exception], ...]: Type[ManagedErrorMixin]} = {
                                         (Exception,): UnsupportedError}):
    try_manage_external_errors(func_to_try=lambda: path_to_resolve.resolve(strict=True),
                               external_errors_to_manage=external_errors_to_manage)
