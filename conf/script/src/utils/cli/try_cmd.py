import argparse
import typing

import utils.error.cls_def
import utils.error.managed


def try_cmd_except_managed_errors(cmd_func: typing.Callable, arg_parser: argparse.ArgumentParser):
    try:
        cmd_func()

    except utils.error.managed.ManagedErrorMixin as raised_error:
        raised_error.raise_or_exit_cli(arg_parser)

    except OSError as raised_error:
        unsupported_error = utils.error.cls_def.UnsupportedError(raised_error)
        unsupported_error.raise_or_exit_cli(arg_parser)
