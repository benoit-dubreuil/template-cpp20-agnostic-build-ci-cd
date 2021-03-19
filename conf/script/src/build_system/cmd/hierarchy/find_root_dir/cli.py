import argparse

import utils.error.cls_def
import utils.error.managed
import utils.error.status
from build_system import cmd
from build_system.cmd.hierarchy.find_root_dir.find_root_dir import VCS_DIR_NAME


def find_root_dir():
    arg_parser = argparse.ArgumentParser(
        description=f"Finds the project's root folder, where the '{VCS_DIR_NAME}' folder is. It searches recursively parent folders upwards.")

    try:
        project_root = cmd.hierarchy.find_root_dir.find_root_dir()
        print(project_root, end=str())

    except utils.error.cls_def.RootDirNotFoundError as raised_error:
        raised_error.raise_or_exit_cli(arg_parser)

    except OSError as raised_error:
        if not isinstance(raised_error, utils.error.managed.ManagedError):
            unsupported_error = utils.error.cls_def.UnsupportedError(raised_error)
            unsupported_error.raise_or_exit_cli(arg_parser)
