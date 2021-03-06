__all__ = ['add_optional_path_arg',
           'parse_optional_path_arg']

import argparse
from pathlib import Path
from typing import AnyStr, Optional

from error import *
from ext.utils.path import *
from .arg import *


def add_optional_path_arg(arg_parser: argparse.ArgumentParser, path_arg: CLIArg = CLIArg.create_default_path_arg(),
                          path_arg_default_value: TUnion_AnyPath = None, path_arg_help: Optional[AnyStr] = None):
    arg_parser.add_argument(path_arg.prefixed_name, type=Path, nargs=argparse.OPTIONAL, const=path_arg_default_value, default=path_arg_default_value, help=path_arg_help)


def _assure_no_unknown_parsed_args(arg_parser: argparse.ArgumentParser, unknown_parsed_args: list[str]):
    if len(unknown_parsed_args) > 0:
        error = UnknownParsedArgError(unknown_parsed_args)
        error.raise_or_exit_cli(arg_parser, print_usage=True)


def _assure_nonempty_parsed_path(arg_parser: argparse.ArgumentParser, path_arg_name: str, parsed_path: TUnion_AnyPath):
    if str(parsed_path) == str():
        error = EmptyParsedArgError(path_arg_name)
        error.raise_or_exit_cli(arg_parser, print_usage=True)


def parse_optional_path_arg(arg_parser: argparse.ArgumentParser, path_arg: CLIArg = CLIArg.create_default_path_arg()) -> TUnion_AnyPath:
    parsed_args, unknown_parsed_args = arg_parser.parse_known_args([path_arg.prefixed_name])

    _assure_no_unknown_parsed_args(arg_parser, unknown_parsed_args)
    parsed_path: TUnion_AnyPath = getattr(parsed_args, path_arg.name) if path_arg.name in parsed_args else None
    _assure_nonempty_parsed_path(arg_parser, path_arg.name, parsed_path)

    return parsed_path
