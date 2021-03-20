import argparse

import utils.error.cls_def
import utils.error.managed
from build_system import cmd
from build_system.cmd.hierarchy.find_build_dir.find_build_dir import BUILD_DIR_NAME


def clean_build_dir():
    arg_parser = argparse.ArgumentParser(
        description=f"Cleans the project's {BUILD_DIR_NAME} folder, where the build system organizes into subfolders specific builds.")
    # TODO
    try:
        cmd.clean_build_dir.clean_build_dir()

    except (utils.error.cls_def.RootDirNotFoundError, utils.error.cls_def.BuildDirNotFoundError) as raised_error:
        raised_error.raise_or_exit_cli(arg_parser)

    except OSError as raised_error:
        if not isinstance(raised_error, utils.error.managed.ManagedError):
            unsupported_error = utils.error.cls_def.UnsupportedError(raised_error)
            unsupported_error.raise_or_exit_cli(arg_parser)
