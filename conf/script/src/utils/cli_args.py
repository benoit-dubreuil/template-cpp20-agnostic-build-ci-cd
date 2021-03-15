import argparse
import sys
from pathlib import Path
from typing import AnyStr, Optional

from utils.cli import DEFAULT_PATH_ARG, format_error_msg
from utils.cli_error import ErrorStatus


def add_optional_path_arg(arg_parser: argparse.ArgumentParser, path_arg: AnyStr = DEFAULT_PATH_ARG, path_arg_default_value: Optional[Path] = None,
                          path_arg_help: Optional[AnyStr] = None):
    arg_parser.add_argument(path_arg, type=str, nargs='?', const=str(), default=path_arg_default_value, help=path_arg_help)


def _assure_no_unknown_parsed_args(arg_parser: argparse.ArgumentParser, unknown_parsed_args: list[str]):
    if len(unknown_parsed_args) > 0:
        error_msg = format_error_msg(f"Unsupported argument '{unknown_parsed_args}'")

        # noinspection PyUnresolvedReferences
        if arg_parser.exit_on_error:
            arg_parser.print_usage(sys.stderr)
            arg_parser.exit(ErrorStatus.UNKNOWN_PARSED_ARG, error_msg)
        else:
            raise TypeError(error_msg)


def _assure_nonempty_parsed_path(arg_parser: argparse.ArgumentParser, path_arg: str, parsed_path: str):
    if parsed_path == str():
        error_msg = format_error_msg(f"'{path_arg}' argument must be followed by a path string")

        # noinspection PyUnresolvedReferences
        if arg_parser.exit_on_error:
            arg_parser.print_usage(sys.stderr)
            arg_parser.exit(ErrorStatus.EMPTY_PARSED_ARG, error_msg)
        else:
            pass  # TODO


def parse_optional_path_arg(arg_parser: argparse.ArgumentParser, path_arg: str = DEFAULT_PATH_ARG) -> Optional[Path]:
    parsed_args, unknown_parsed_args = arg_parser.parse_known_args(path_arg)

    _assure_no_unknown_parsed_args(arg_parser, unknown_parsed_args)
    parsed_path: Optional[str] = parsed_args[path_arg]

    if parsed_path == str():
        error_msg = format_error_msg(f"'{path_arg}' argument must be followed by a path string")
        arg_parser.error(error_msg)

    return Path(parsed_path) if parsed_path is not None else None
