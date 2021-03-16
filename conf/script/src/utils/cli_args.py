import argparse
import sys
from pathlib import Path
from typing import AnyStr, Final, Optional

import utils.cli_error
import utils.formatted_error

DEFAULT_PATH_ARG_NAME: Final[str] = 'path'
DEFAULT_PATH_ARG: Final[str] = '-' + DEFAULT_PATH_ARG_NAME


def add_optional_path_arg(arg_parser: argparse.ArgumentParser, path_arg: AnyStr = DEFAULT_PATH_ARG, path_arg_default_value: Optional[Path] = None,
                          path_arg_help: Optional[AnyStr] = None):
    arg_parser.add_argument(path_arg, type=str, nargs='?', const=str(), default=path_arg_default_value, help=path_arg_help)


def _assure_no_unknown_parsed_args(arg_parser: argparse.ArgumentParser, unknown_parsed_args: list[str]):
    if len(unknown_parsed_args) > 0:
        error = utils.cli_error.UnknownParsedArgError(unknown_parsed_args)

        # noinspection PyUnresolvedReferences
        if arg_parser.exit_on_error:
            arg_parser.print_usage(sys.stderr)
            arg_parser.exit(utils.cli_error.ErrorStatus.UNKNOWN_PARSED_ARG, str(error))
        else:
            raise error


def _assure_nonempty_parsed_path(arg_parser: argparse.ArgumentParser, path_arg: str, parsed_path: str):
    if parsed_path == str():
        error_msg = utils.formatted_error.format_exception_msg(f"'{path_arg}' argument must be followed by a path string")

        # noinspection PyUnresolvedReferences
        if arg_parser.exit_on_error:
            arg_parser.print_usage(sys.stderr)
            arg_parser.exit(utils.cli_error.ErrorStatus.EMPTY_PARSED_ARG, error_msg)
        else:
            pass  # TODO


def parse_optional_path_arg(arg_parser: argparse.ArgumentParser, path_arg: str = DEFAULT_PATH_ARG) -> Optional[Path]:
    parsed_args, unknown_parsed_args = arg_parser.parse_known_args(path_arg)

    _assure_no_unknown_parsed_args(arg_parser, unknown_parsed_args)
    parsed_path: Optional[str] = parsed_args[path_arg]

    if parsed_path == str():
        error_msg = format_exception_msg(f"'{path_arg}' argument must be followed by a path string")
        arg_parser.error(error_msg)

    return Path(parsed_path) if parsed_path is not None else None
