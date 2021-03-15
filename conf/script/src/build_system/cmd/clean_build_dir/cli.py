import argparse
from typing import Final

import build_system.cmd.hierarchy.find_root_dir
import build_system.cmd.hierarchy.find_root_dir.cli
from build_system import cmd

ANY_BUILD_DIR_NOT_FOUND_ERROR_STATUS: Final[int] = 1 + cmd.hierarchy.find_root_dir.cli.ROOT_NOT_FOUND_ERROR_STATUS
UNSUPPORTED_ERROR_STATUS: Final[int] = 1 + ANY_BUILD_DIR_NOT_FOUND_ERROR_STATUS


def clean_build_dir():
    arg_parser = argparse.ArgumentParser(
        description=f"Cleans the project's build folder, where the build system organizes into subfolders specific builds.")

    root_dir = None

    try:
        try:
            root_dir = cmd.hierarchy.find_root_dir.find_root_dir()
        except FileNotFoundError as raised_exception:
            arg_parser.exit(cmd.hierarchy.find_root_dir.cli.ROOT_NOT_FOUND_ERROR_STATUS, str(raised_exception))

        try:
            cmd.clean_build_dir.clean_build_dir(root_dir)
        except FileNotFoundError as raised_exception:
            arg_parser.exit(ANY_BUILD_DIR_NOT_FOUND_ERROR_STATUS, str(raised_exception))

    except OSError as raised_exception:
        arg_parser.exit(UNSUPPORTED_ERROR_STATUS, str(raised_exception))
