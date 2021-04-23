import argparse

import colorama

import build_system.cmd.hierarchy.consts
import build_system.cmd.hierarchy.create_targets_build_dirs
import ext.cli.arg_parsing
import ext.cli.try_cmd
from ext.more_typing import AnyPath


def create_target_build_dirs():
    arg_parser = argparse.ArgumentParser(description="Creates the project's target build directories inside the "
                                                     f"'{colorama.Fore.LIGHTBLACK_EX}{build_system.cmd.hierarchy.consts.BUILD_DIR_NAME}{colorama.Style.RESET_ALL}' folder.")

    ext.cli.arg_parsing.add_optional_path_arg(arg_parser=arg_parser,
                                              path_arg=build_system.cmd.hierarchy.consts.BUILD_DIR_ARG,
                                              path_arg_help=f"The project's {build_system.cmd.hierarchy.consts.BUILD_DIR_NAME} directory")

    build_dir: AnyPath = ext.cli.arg_parsing.parse_optional_path_arg(arg_parser, build_system.cmd.hierarchy.consts.BUILD_DIR_ARG)
    arg_parser.parse_args()

    def cli_cmd():
        build_system.cmd.hierarchy.create_targets_build_dirs.create_targets_build_dirs(build_dir)

    ext.cli.try_cmd.try_cmd_except_managed_errors(cli_cmd, arg_parser)
