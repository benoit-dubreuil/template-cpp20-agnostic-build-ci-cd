import utils.cli
from build_system.cmd import hierarchy
from pathlib import Path
import argparse


def get_error_formatted_msg_root_not_found() -> str:
    return utils.cli.format_error_msg(hierarchy.find_root.get_error_msg_root_not_found())


def find_root():
    arg_parser = argparse.ArgumentParser(
        description=f"Fetches the project's root folder, where the '{hierarchy.find_root.VCS_DIR_NAME}' is. It searches recursively parent folders upwards.")

    try:
        project_root: Path = hierarchy.find_root.find_root_dir(get_error_formatted_msg_root_not_found)
        print(project_root)
    except FileNotFoundError as raised_exception:
        raised_exception_msg = str(raised_exception)
        arg_parser.error(raised_exception_msg)
