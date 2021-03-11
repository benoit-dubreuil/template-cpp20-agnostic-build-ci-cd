import utils.cli
from build_system.cmd import hierarchy
from pathlib import Path
import argparse


def get_error_formatted_msg_root_not_found() -> str:
    return utils.cli.format_error_msg(hierarchy.find_root.get_error_msg_root_not_found())


def find_root() -> Path:
    arg_parser = argparse.ArgumentParser(
        description=f"Fetches the project's root folder, where the '{hierarchy.find_root.VCS_DIR_NAME}' is. It searches recursively parent folders upwards.")

    try:
        return hierarchy.find_root.find_root(get_error_formatted_msg_root_not_found)
    except FileNotFoundError as raised_exception:
        raised_exception_msg = str(raised_exception)
        arg_parser.error(raised_exception_msg)
