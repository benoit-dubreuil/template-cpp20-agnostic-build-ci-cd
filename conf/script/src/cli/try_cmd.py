__all__ = ['try_cmd_except_managed_errors']

import argparse
from typing import Callable

from ..error import *


def try_cmd_except_managed_errors(cmd_func: Callable, arg_parser: argparse.ArgumentParser):
    try:
        cmd_func()

    except ManagedErrorMixin as raised_error:
        raised_error.raise_or_exit_cli(arg_parser)

    except OSError as raised_error:
        unsupported_error = UnsupportedError(raised_error)
        unsupported_error.raise_or_exit_cli(arg_parser)
