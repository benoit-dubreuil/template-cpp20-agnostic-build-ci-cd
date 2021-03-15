import argparse
from pathlib import Path

from build_system.cmd import hierarchy
from build_system.cmd.hierarchy.find_root_dir.find_root_dir import VCS_DIR_NAME

ROOT_NOT_FOUND_ERROR_STATUS = 1


def find_root_dir():
    arg_parser = argparse.ArgumentParser(
        description=f"Fetches the project's root folder, where the '{VCS_DIR_NAME}' is. It searches recursively parent folders upwards.")

    try:
        project_root: Path = hierarchy.find_root_dir.find_root_dir()
        print(project_root, end=str())
    except FileNotFoundError as raised_exception:
        raised_exception_msg = str(raised_exception)
        arg_parser.exit(ROOT_NOT_FOUND_ERROR_STATUS, raised_exception_msg)
