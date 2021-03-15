import argparse
from pathlib import Path
from typing import Final

from build_system.cmd import hierarchy
from build_system.cmd.hierarchy.find_root_dir.find_root_dir import VCS_DIR_NAME

ROOT_NOT_FOUND_ERROR_STATUS: Final[int] = 1
UNSUPPORTED_ERROR_STATUS: Final[int] = 1 + ROOT_NOT_FOUND_ERROR_STATUS


def find_root_dir():
    arg_parser = argparse.ArgumentParser(
        description=f"Fetches the project's root folder, where the '{VCS_DIR_NAME}' is. It searches recursively parent folders upwards.")

    try:
        try:
            project_root: Path = hierarchy.find_root_dir.find_root_dir()
            print(project_root, end=str())
        except FileNotFoundError as raised_exception:
            arg_parser.exit(ROOT_NOT_FOUND_ERROR_STATUS, str(raised_exception))

    except OSError as raised_exception:
        arg_parser.exit(UNSUPPORTED_ERROR_STATUS, str(raised_exception))
