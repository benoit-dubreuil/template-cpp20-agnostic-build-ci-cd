__all__ = ['cli_find_build_dir']

import argparse

import colorama

from cli import *
from ext.utils.path import *
from file_structure import *
from .impl import *


def cli_find_build_dir():
    arg_parser = argparse.ArgumentParser(
        description=f"Finds the project's '{colorama.Fore.LIGHTBLACK_EX}{BUILD_DIR_NAME}{colorama.Style.RESET_ALL}' folder.")
    add_optional_path_arg(arg_parser, ROOT_DIR_ARG, path_arg_help="The project's root directory")

    root_dir: AnyPath = parse_optional_path_arg(arg_parser, ROOT_DIR_ARG)
    arg_parser.parse_args()

    def cli_cmd():
        build_dir = find_build_dir(root_dir)
        print(build_dir, end=str())

    try_cmd_except_managed_errors(cli_cmd, arg_parser)
