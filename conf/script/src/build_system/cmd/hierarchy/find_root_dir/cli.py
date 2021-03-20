import argparse

import utils.error.cls_def
import utils.error.managed
from build_system import cmd
from build_system.cmd.hierarchy.find_root_dir.find_root_dir import BUILD_SYSTEM_CONF_FILENAME


def find_root_dir():
    arg_parser = argparse.ArgumentParser(
        description=f"Finds the project's root folder, where the '{BUILD_SYSTEM_CONF_FILENAME}' folder is. It searches recursively parent folders upwards.")

    try:
        project_root = cmd.hierarchy.find_root_dir.find_root_dir()
        print(project_root, end=str())

    except utils.error.cls_def.RootDirNotFoundError as raised_error:
        raised_error.raise_or_exit_cli(arg_parser)

    except OSError as raised_error:
        if not isinstance(raised_error, utils.error.managed.ManagedErrorMixin):
            unsupported_error = utils.error.cls_def.UnsupportedError(raised_error)
            unsupported_error.raise_or_exit_cli(arg_parser)
