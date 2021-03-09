import argparse
from pathlib import Path
from typing import Callable

import colorama

from compiler_version import CompilerVersion
from data_model import Compiler


def cli_init():
    colorama.init()


def cli_fetch_compiler_version(compiler: Compiler, fetch_compiler_version_func: Callable[[Path or None], CompilerVersion], default_compiler_path: Path or None = None) -> None:
def cli_fetch_compiler_version(compiler: Compiler, default_compiler_path: Path or None, fetch_compiler_version_func: Callable[[Path], CompilerVersion]) -> None:
    compiler_arg = compiler.value

    arg_parser = argparse.ArgumentParser(description=f'Fetches {compiler.name} compiler\'s version')
    arg_parser.add_argument(compiler_arg, type=Path, nargs='?', const=default_compiler_path, default=default_compiler_path, help=f'The {compiler.name} compiler\'s executable path')

    args = arg_parser.parse_args()
    compiler_path: Path or None = getattr(args, compiler_arg)
    compiler_version = fetch_compiler_version_func(compiler_path)

    print(compiler_version, end='')


def cli_fetch_compiler_version_with_default_path(compiler: Compiler, fetch_compiler_version_func: Callable[[Path], CompilerVersion]) -> None:
def cli_fetch_compiler_version(compiler: Compiler, fetch_compiler_version_func: Callable[[Path], CompilerVersion]) -> None:
    cli_fetch_compiler_version(compiler, compiler.value, fetch_compiler_version_func)
