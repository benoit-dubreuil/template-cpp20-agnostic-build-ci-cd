import argparse

import colorama

import build_system.cmd.hierarchy.find_build_dir
import utils.cli.try_cmd


def setup():
    arg_parser = argparse.ArgumentParser(
        description=f"Creates the '{colorama.Fore.LIGHTBLACK_EX}{build_system.cmd.hierarchy.find_build_dir.BUILD_DIR_NAME}{colorama.Style.RESET_ALL}'"
                    'folder and setup specific build system builds inside.')

    # TODO

    def cli_cmd():
        build_system.cmd.setup.setup_build_system()

    utils.cli.try_cmd.try_cmd_except_managed_errors(cli_cmd, arg_parser)
