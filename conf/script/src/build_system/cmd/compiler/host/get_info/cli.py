import argparse
from pathlib import Path
from typing import Any, Callable, Optional

import build_system.compiler.core.family
import ext.cli.arg_parsing
import ext.cli.try_cmd


def fetch_compiler_info(compiler_family: build_system.compiler.core.family.CompilerFamily,
                        fetch_compiler_info_func: Callable[[Optional[Path]], Any],
                        default_compiler_path: Optional[Path] = None,
                        desc_compiler_info: str = 'version',
                        help_path_meaning: str = 'executable') -> None:
    arg_parser = argparse.ArgumentParser(description=f"Fetches {compiler_family.name} compiler's {desc_compiler_info}")
    ext.cli.arg_parsing.add_optional_path_arg(arg_parser, path_arg_default_value=default_compiler_path,
                                              path_arg_help=f"The {compiler_family.name} compiler's {help_path_meaning} path")

    compiler_path: Optional[Path] = ext.cli.arg_parsing.parse_optional_path_arg(arg_parser)
    arg_parser.parse_args()

    def cli_cmd():
        compiler_info = fetch_compiler_info_func(compiler_path)
        print(compiler_info, end=str())

    ext.cli.try_cmd.try_cmd_except_managed_errors(cli_cmd, arg_parser)


def fetch_compiler_info_with_default_path(compiler_family: build_system.compiler.core.family.CompilerFamily, fetch_compiler_info_func: Callable[[Path], Any]) -> None:
    fetch_compiler_info(compiler_family, fetch_compiler_info_func, compiler_family.value)
