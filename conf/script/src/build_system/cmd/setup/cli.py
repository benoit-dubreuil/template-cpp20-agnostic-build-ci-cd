import argparse

import colorama

import build_system.cmd.hierarchy.consts
import utils.cli.arg_parsing
import utils.cli.try_cmd
from utils.more_typing import AnyPath


def setup():
    # TODO : Fix description
    arg_parser = argparse.ArgumentParser(description=f"Creates the '{colorama.Fore.LIGHTBLACK_EX}{build_system.cmd.hierarchy.consts.BUILD_DIR_NAME}{colorama.Style.RESET_ALL}'"
                                                     'folder and setup specific build system builds inside.')
    utils.cli.arg_parsing.add_optional_path_arg(arg_parser, build_system.cmd.hierarchy.consts.ROOT_DIR_ARG, path_arg_help="The project's root directory")

    root_dir: AnyPath = utils.cli.arg_parsing.parse_optional_path_arg(arg_parser, build_system.cmd.hierarchy.consts.ROOT_DIR_ARG)
    arg_parser.parse_args()

    def cli_cmd():
        build_system.cmd.setup.setup_build_system(root_dir)

    utils.cli.try_cmd.try_cmd_except_managed_errors(cli_cmd, arg_parser)
