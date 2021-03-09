import argparse
from pathlib import Path

from data_model import Compiler
from fetch_gnu_compiler_version import fetch_gnu_compiler_version


def cli_fetch_gnu_compiler_version(compiler: Compiler):
    compiler_arg = compiler.value

    arg_parser = argparse.ArgumentParser(description=f'Fetches {compiler.name} compiler\'s version')
    arg_parser.add_argument(compiler_arg, type=Path, nargs='?', const=compiler_arg, default=compiler_arg, help=f'The {compiler.name} compiler\'s executable path')

    args = arg_parser.parse_args()
    compiler_path = getattr(args, compiler_arg)

    print(fetch_gnu_compiler_version(compiler_path), end='')
