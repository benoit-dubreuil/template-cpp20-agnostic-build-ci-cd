import argparse
from build_system import cmd
import build_system.cmd.hierarchy.find_root_dir


def clean_build_dir():
    arg_parser = argparse.ArgumentParser(
        description=f"Cleans the project's build folder, where the build system organizes into subfolders specific builds.")

    try:
        cmd.hierarchy.find_root_dir.find_root_dir()
    except FileNotFoundError as raised_exception:
        pass

    try:
        cmd.clean_build_dir.clean_build_dir()
    except FileNotFoundError as raised_exception:
        pass
