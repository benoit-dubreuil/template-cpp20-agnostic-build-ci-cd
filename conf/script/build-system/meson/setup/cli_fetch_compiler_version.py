import argparse
from pathlib import Path
from typing import Callable, Optional, Final, AnyStr

import colorama

from compiler_version import CompilerVersion
from data_model import Compiler


def cli_init():
    colorama.init()


def format_error_msg(error_msg: AnyStr) -> AnyStr:
    return colorama.Style.BRIGHT + colorama.Fore.RED + error_msg + colorama.Style.RESET_ALL


def cli_fetch_compiler_version(compiler: Compiler, fetch_compiler_version_func: Callable[[Optional[Path]], CompilerVersion], default_compiler_path: Optional[Path] = None,
                               help_path_meaning: str = 'executable') -> None:
    path_arg_name: Final[str] = 'path'
    path_arg: Final[str] = '-' + path_arg_name

    arg_parser = argparse.ArgumentParser(description=f'Fetches {compiler.name} compiler\'s version')
    arg_parser.add_argument(path_arg, type=str, nargs='?', const=str(), default=default_compiler_path,
                            help=f'The {compiler.name} compiler\'s {help_path_meaning} {path_arg_name}')

    args = arg_parser.parse_args()
    compiler_path: Optional[str] = getattr(args, path_arg_name)

    if compiler_path == str():
        error_msg = format_error_msg(f"'{path_arg}' argument must be followed by a path string")
        arg_parser.error(error_msg)

    compiler_path: Optional[Path] = Path(compiler_path) if compiler_path is not None else None

    try:
        compiler_version = fetch_compiler_version_func(compiler_path)
        print(compiler_version, end='')
    except FileNotFoundError as exception:
        arg_parser.error(str(exception))


def cli_fetch_compiler_version_with_default_path(compiler: Compiler, fetch_compiler_version_func: Callable[[Path], CompilerVersion]) -> None:
    cli_fetch_compiler_version(compiler, fetch_compiler_version_func, compiler.value)
