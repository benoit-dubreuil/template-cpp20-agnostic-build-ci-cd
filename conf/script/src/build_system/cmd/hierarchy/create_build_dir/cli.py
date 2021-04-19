import argparse

import colorama

import build_system.cmd.hierarchy.consts
import build_system.cmd.hierarchy.create_build_dir
import ext.cli.arg_parsing
import ext.cli.try_cmd
from ext.more_typing import AnyPath


def create_build_dir():
    arg_parser = argparse.ArgumentParser(
        description=f"Creates the project's '{colorama.Fore.LIGHTBLACK_EX}{build_system.cmd.hierarchy.consts.BUILD_DIR_NAME}{colorama.Style.RESET_ALL}' folder.")
    ext.cli.arg_parsing.add_optional_path_arg(arg_parser, build_system.cmd.hierarchy.consts.ROOT_DIR_ARG, path_arg_help="The project's root directory")

    root_dir: AnyPath = ext.cli.arg_parsing.parse_optional_path_arg(arg_parser, build_system.cmd.hierarchy.consts.ROOT_DIR_ARG)
    arg_parser.parse_args()

    def cli_cmd():
        build_system.cmd.hierarchy.create_build_dir.create_build_dir(root_dir)

    ext.cli.try_cmd.try_cmd_except_managed_errors(cli_cmd, arg_parser)
