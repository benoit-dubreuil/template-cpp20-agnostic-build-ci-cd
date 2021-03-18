import argparse

import utils.cli.error
from build_system import cmd
from build_system.cmd.hierarchy.find_root_dir.find_root_dir import VCS_DIR_NAME


def find_root_dir():
    arg_parser = argparse.ArgumentParser(
        description=f"Finds the project's root folder, where the '{VCS_DIR_NAME}' folder is. It searches recursively parent folders upwards.")

    try:
        project_root = cmd.hierarchy.find_root_dir.find_root_dir()
        print(project_root, end=str())

    except cmd.hierarchy.find_root_dir.error.RootDirNotFoundError as raised_exception:
        arg_parser.exit(utils.cli.error.ErrorStatus.ROOT_DIR_NOT_FOUND, str(raised_exception))

    except OSError as raised_exception:
        arg_parser.exit(utils.cli.error.ErrorStatus.UNSUPPORTED_ERROR, str(raised_exception))
