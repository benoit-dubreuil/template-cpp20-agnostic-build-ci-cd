import argparse
from pathlib import Path
from typing import Any, Callable, Final, Optional

import utils.cli
import utils.cli_arg_parser
from build_system.compiler.family import CompilerFamily

COMPILER_NOT_FOUND_ERROR_STATUS: Final[int] = 1


def cli_fetch_compiler_info(compiler_family: CompilerFamily, fetch_compiler_info_func: Callable[[Optional[Path]], Any], default_compiler_path: Optional[Path] = None,
                            desc_compiler_info: str = 'version', help_path_meaning: str = 'executable') -> None:
    arg_parser = argparse.ArgumentParser(description=f"Fetches {compiler_family.name} compiler's {desc_compiler_info}")
    utils.cli_arg_parser.add_optional_path_arg(arg_parser, path_arg_default_value=default_compiler_path, path_arg_help=f"The {compiler_family.name} compiler's {help_path_meaning} path")

    compiler_path: Optional[Path] = utils.cli_arg_parser.parse_optional_path_arg(arg_parser)

    try:
        compiler_info = fetch_compiler_info_func(compiler_path)
        print(compiler_info, end=str())
    except FileNotFoundError as exception:
        arg_parser.exit(COMPILER_NOT_FOUND_ERROR_STATUS, str(exception))


def cli_fetch_compiler_info_with_default_path(compiler_family: CompilerFamily, fetch_compiler_info_func: Callable[[Path], Any]) -> None:
    cli_fetch_compiler_info(compiler_family, fetch_compiler_info_func, compiler_family.value)
