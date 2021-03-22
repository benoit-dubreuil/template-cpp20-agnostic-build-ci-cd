import argparse

import build_system.cmd.hierarchy.find_root_dir
import utils.cli.try_cmd


def find_root_dir():
    arg_parser = argparse.ArgumentParser(
        description=f"Finds the project's root folder, where the '{build_system.cmd.hierarchy.find_root_dir.BUILD_SYSTEM_CONF_FILENAME}' folder is. "
                    'It searches recursively parent folders upwards.')

    def cli_cmd():
        project_root = build_system.cmd.hierarchy.find_root_dir.find_root_dir()
        print(project_root, end=str())

    utils.cli.try_cmd.try_cmd_except_managed_errors(cli_cmd, arg_parser)
