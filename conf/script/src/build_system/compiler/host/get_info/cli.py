import argparse
from pathlib import Path
from typing import Any, Callable, Final, Optional

from build_system.compiler.family import CompilerFamily
from src.utils import format_error_msg


def cli_fetch_compiler_info(compiler_family: CompilerFamily, fetch_compiler_info_func: Callable[[Optional[Path]], Any], default_compiler_path: Optional[Path] = None,
                            desc_compiler_info: str = 'version', help_path_meaning: str = 'executable') -> None:
    path_arg_name: Final[str] = 'path'
    path_arg: Final[str] = '-' + path_arg_name

    arg_parser = argparse.ArgumentParser(description=f'Fetches {compiler_family.name} compiler\'s {desc_compiler_info}')
    arg_parser.add_argument(path_arg, type=str, nargs='?', const=str(), default=default_compiler_path,
                            help=f'The {compiler_family.name} compiler\'s {help_path_meaning} {path_arg_name}')

    args = arg_parser.parse_args()
    compiler_path: Optional[str] = getattr(args, path_arg_name)

    if compiler_path == str():
        error_msg = format_error_msg(f"'{path_arg}' argument must be followed by a path string")
        arg_parser.error(error_msg)

    compiler_path: Optional[Path] = Path(compiler_path) if compiler_path is not None else None

    try:
        compiler_info = fetch_compiler_info_func(compiler_path)
        print(compiler_info, end='')
    except FileNotFoundError as exception:
        arg_parser.error(str(exception))


def cli_fetch_compiler_info_with_default_path(compiler_family: CompilerFamily, fetch_compiler_info_func: Callable[[Path], Any]) -> None:
    cli_fetch_compiler_info(compiler_family, fetch_compiler_info_func, compiler_family.value)
