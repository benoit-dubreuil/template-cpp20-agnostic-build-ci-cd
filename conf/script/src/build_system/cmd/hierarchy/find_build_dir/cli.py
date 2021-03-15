import argparse
from typing import Final

import build_system.cmd.hierarchy.find_root_dir.cli
from build_system import cmd
from build_system.cmd.hierarchy.find_build_dir.find_build_dir import BUILD_DIR_NAME

BUILD_DIR_NOT_FOUND_ERROR_STATUS: Final[int] = 1 + cmd.hierarchy.find_root_dir.cli.ROOT_DIR_NOT_FOUND_ERROR_STATUS
UNSUPPORTED_ERROR_STATUS: Final[int] = 1 + BUILD_DIR_NOT_FOUND_ERROR_STATUS


def find_build_dir():
    arg_parser = argparse.ArgumentParser(
        description=f"Finds the project's '{BUILD_DIR_NAME}' folder.")

    try:
        build_dir = cmd.hierarchy.find_build_dir.find_build_dir()
        print(build_dir, end=str())

    except cmd.hierarchy.find_root_dir.error.RootDirNotFoundError as raised_exception:
        arg_parser.exit(cmd.hierarchy.find_root_dir.cli.ROOT_DIR_NOT_FOUND_ERROR_STATUS, str(raised_exception))

    except cmd.hierarchy.find_build_dir.error.BuildDirNotFoundError as raised_exception:
        arg_parser.exit(BUILD_DIR_NOT_FOUND_ERROR_STATUS, str(raised_exception))

    except OSError as raised_exception:
        arg_parser.exit(UNSUPPORTED_ERROR_STATUS, str(raised_exception))
