import argparse

import build_system.cmd.hierarchy.find_root_dir
import utils.error.error
import utils.error.status
from build_system import cmd


def clean_build_dir():
    arg_parser = argparse.ArgumentParser(
        description=f"Cleans the project's build folder, where the build system organizes into subfolders specific builds.")

    root_dir = None

    try:
        try:
            root_dir = cmd.hierarchy.find_root_dir.find_root_dir()
        except utils.error.error.RootDirNotFoundError as raised_exception:
            arg_parser.exit(utils.error.status.ErrorStatus.ROOT_DIR_NOT_FOUND, str(raised_exception))

        try:
            cmd.clean_build_dir.clean_build_dir(root_dir)
        except FileNotFoundError as raised_exception:
            arg_parser.exit(utils.error.status.ErrorStatus.BUILD_DIR_NOT_FOUND, str(raised_exception))

    except OSError as raised_exception:
        arg_parser.exit(utils.error.status.ErrorStatus.UNSUPPORTED, str(raised_exception))
