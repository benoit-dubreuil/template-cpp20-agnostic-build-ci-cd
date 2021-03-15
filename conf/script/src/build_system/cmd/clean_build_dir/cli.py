import argparse
from build_system import cmd


def clean_build_dir():
    arg_parser = argparse.ArgumentParser(
        description=f"Cleans the project's build folder, where the build system organizes into subfolders specific builds.")

    try:
        cmd.clean_build_dir.clean_build_dir()
    except FileNotFoundError as raised_exception:
        pass
