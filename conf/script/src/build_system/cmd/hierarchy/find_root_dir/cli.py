__all__ = ['cli_find_root_dir']

import argparse

import colorama

from ext.cli import *
from file_structure import *
from .impl import *


def cli_find_root_dir():
    arg_parser = argparse.ArgumentParser(
        description="Finds the project's root folder, where the "
                    f"'{colorama.Fore.LIGHTBLACK_EX}{BUILD_SYSTEM_CONF_FILE_NAME}{colorama.Style.RESET_ALL}' folder is. "
                    'It searches recursively parent folders upwards.')

    arg_parser.parse_args()

    def cli_cmd():
        project_root = find_root_dir()
        print(project_root, end=str())

    try_cmd_except_managed_errors(cli_cmd, arg_parser)
