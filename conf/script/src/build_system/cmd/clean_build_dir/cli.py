import argparse

import utils.error.cls_def
import utils.error.managed
import utils.error.status
from build_system import cmd


def clean_build_dir():
    arg_parser = argparse.ArgumentParser(
        description=f"Cleans the project's build folder, where the build system organizes into subfolders specific builds.")

    try:
        cmd.clean_build_dir.clean_build_dir()

    except (utils.error.cls_def.RootDirNotFoundError, utils.error.cls_def.BuildDirNotFoundError) as raised_error:
        raised_error.raise_or_exit_cli(arg_parser)

    except OSError as raised_error:
        if not isinstance(raised_error, utils.error.managed.ManagedError):
            unsupported_error = utils.error.cls_def.UnsupportedError(raised_error)
            unsupported_error.raise_or_exit_cli(arg_parser)
