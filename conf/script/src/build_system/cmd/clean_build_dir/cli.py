import argparse
from build_system import cmd
import build_system.cmd.hierarchy.find_root_dir
import build_system.cmd.hierarchy.find_root_dir.cli


def clean_build_dir():
    arg_parser = argparse.ArgumentParser(
        description=f"Cleans the project's build folder, where the build system organizes into subfolders specific builds.")

    root_dir = None

    try:
        root_dir = cmd.hierarchy.find_root_dir.find_root_dir()
    except FileNotFoundError as raised_exception:
        raised_exception_msg = str(raised_exception)
        arg_parser.exit(cmd.hierarchy.find_root_dir.cli.ROOT_NOT_FOUND_ERROR_STATUS, raised_exception_msg)

    try:
        cmd.clean_build_dir.clean_build_dir(root_dir)
    except FileNotFoundError as raised_exception:
        pass
