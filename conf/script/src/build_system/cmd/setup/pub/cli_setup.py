__all__ = ['cli_setup_build_system']

import argparse

import colorama

from cli import *
from ext.utils.more_typing import *
from file_structure import *
from .setup import *


def cli_setup_build_system():
    # TODO : Fix description
    arg_parser = argparse.ArgumentParser(description=f"Creates the '{colorama.Fore.LIGHTBLACK_EX}{BUILD_DIR_NAME}{colorama.Style.RESET_ALL}'"
                                                     'folder and setup specific build system builds inside.')
    add_optional_path_arg(arg_parser, ROOT_DIR_ARG, path_arg_help="The project's root directory")

    root_dir: AnyPath = parse_optional_path_arg(arg_parser, ROOT_DIR_ARG)
    arg_parser.parse_args()

    def cli_cmd():
        setup_build_system(root_dir=root_dir, cli_mode=True)

    try_cmd_except_managed_errors(cli_cmd, arg_parser)
