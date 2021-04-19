import argparse
import typing

from ..meta_prog.encapsulation import *
from ..error import *


@export
def try_cmd_except_managed_errors(cmd_func: typing.Callable, arg_parser: argparse.ArgumentParser):
    try:
        cmd_func()

    except ManagedErrorMixin as raised_error:
        raised_error.raise_or_exit_cli(arg_parser)

    except OSError as raised_error:
        unsupported_error = UnsupportedError(raised_error)
        unsupported_error.raise_or_exit_cli(arg_parser)
