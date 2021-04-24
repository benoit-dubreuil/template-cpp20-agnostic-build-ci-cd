__all__ = ['cli_create_build_dir']

import argparse

import colorama

from build_system.cmd.hierarchy.consts import *
from build_system.cmd.hierarchy.create_build_dir import *
from ext.cli import *
from ext.more_typing import AnyPath


def cli_create_build_dir():
    arg_parser = argparse.ArgumentParser(
        description=f"Creates the project's '{colorama.Fore.LIGHTBLACK_EX}{BUILD_DIR_NAME}{colorama.Style.RESET_ALL}' folder.")
    add_optional_path_arg(arg_parser, ROOT_DIR_ARG, path_arg_help="The project's root directory")

    root_dir: AnyPath = parse_optional_path_arg(arg_parser, ROOT_DIR_ARG)
    arg_parser.parse_args()

    def cli_cmd():
        create_build_dir(root_dir=root_dir)

    try_cmd_except_managed_errors(cli_cmd, arg_parser)
