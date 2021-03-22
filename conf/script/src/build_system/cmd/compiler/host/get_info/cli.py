import argparse
from pathlib import Path
from typing import Any, Callable, Optional

import build_system.compiler.family
import utils.cli.arg_parsing
import utils.error.cls_def
import utils.error.managed


def fetch_compiler_info(compiler_family: build_system.compiler.family.CompilerFamily,
                        fetch_compiler_info_func: Callable[[Optional[Path]], Any],
                        default_compiler_path: Optional[Path] = None,
                        desc_compiler_info: str = 'version',
                        help_path_meaning: str = 'executable') -> None:
    arg_parser = argparse.ArgumentParser(description=f"Fetches {compiler_family.name} compiler's {desc_compiler_info}")
    utils.cli.arg_parsing.add_optional_path_arg(arg_parser, path_arg_default_value=default_compiler_path,
                                                path_arg_help=f"The {compiler_family.name} compiler's {help_path_meaning} path")

    compiler_path: Optional[Path] = utils.cli.arg_parsing.parse_optional_path_arg(arg_parser)

    try:
        compiler_info = fetch_compiler_info_func(compiler_path)
        print(compiler_info, end=str())

    except utils.error.managed.ManagedErrorMixin as raised_error:
        raised_error.raise_or_exit_cli(arg_parser)

    except OSError as raised_error:
        unsupported_error = utils.error.cls_def.UnsupportedError(raised_error)
        unsupported_error.raise_or_exit_cli(arg_parser)


def fetch_compiler_info_with_default_path(compiler_family: build_system.compiler.family.CompilerFamily, fetch_compiler_info_func: Callable[[Path], Any]) -> None:
    fetch_compiler_info(compiler_family, fetch_compiler_info_func, compiler_family.value)
