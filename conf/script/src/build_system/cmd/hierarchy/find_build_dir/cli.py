import argparse
from typing import Final

import build_system.cmd.hierarchy.find_root_dir.cli
import utils.cli.arg
import utils.cli.arg_parsing
from build_system import cmd
from build_system.cmd.hierarchy.find_build_dir.find_build_dir import BUILD_DIR_NAME
from utils.more_typing import AnyPath

BUILD_DIR_NOT_FOUND_ERROR_STATUS: Final[int] = 1 + cmd.hierarchy.find_root_dir.cli.ROOT_DIR_NOT_FOUND_ERROR_STATUS
UNSUPPORTED_ERROR_STATUS: Final[int] = 1 + BUILD_DIR_NOT_FOUND_ERROR_STATUS

ROOT_DIR_ARG: Final[utils.cli.arg.CLIArg] = utils.cli.arg.CLIArg('rootdir')


def find_build_dir():
    arg_parser = argparse.ArgumentParser(description=f"Finds the project's '{BUILD_DIR_NAME}' folder.")
    utils.cli.arg_parsing.add_optional_path_arg(arg_parser, ROOT_DIR_ARG, path_arg_help=f"The project's root directory")

    root_dir: AnyPath = utils.cli.arg_parsing.parse_optional_path_arg(arg_parser, ROOT_DIR_ARG)

    try:
        build_dir = cmd.hierarchy.find_build_dir.find_build_dir()
        print(build_dir, end=str())

    except cmd.hierarchy.find_root_dir.error.RootDirNotFoundError as raised_exception:
        arg_parser.exit(cmd.hierarchy.find_root_dir.cli.ROOT_DIR_NOT_FOUND_ERROR_STATUS, str(raised_exception))

    except cmd.hierarchy.find_build_dir.error.BuildDirNotFoundError as raised_exception:
        arg_parser.exit(BUILD_DIR_NOT_FOUND_ERROR_STATUS, str(raised_exception))

    except OSError as raised_exception:
        arg_parser.exit(UNSUPPORTED_ERROR_STATUS, str(raised_exception))
