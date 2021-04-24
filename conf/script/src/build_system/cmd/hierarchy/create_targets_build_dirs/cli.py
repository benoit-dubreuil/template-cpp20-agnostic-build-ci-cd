__all__ = ['cli_create_target_build_dirs']

import argparse

import colorama

from ext.cli import *
from ext.more_typing import *
from .impl import *
from ..consts import *


def cli_create_target_build_dirs():
    arg_parser = argparse.ArgumentParser(description="Creates the project's target build directories inside the "
                                                     f"'{colorama.Fore.LIGHTBLACK_EX}{BUILD_DIR_NAME}{colorama.Style.RESET_ALL}' folder.")

    add_optional_path_arg(arg_parser=arg_parser,
                          path_arg=BUILD_DIR_ARG,
                          path_arg_help=f"The project's {BUILD_DIR_NAME} directory")

    build_dir: AnyPath = parse_optional_path_arg(arg_parser, BUILD_DIR_ARG)
    arg_parser.parse_args()

    def cli_cmd():
        create_targets_build_dirs_structure(build_dir)

    try_cmd_except_managed_errors(cli_cmd, arg_parser)
