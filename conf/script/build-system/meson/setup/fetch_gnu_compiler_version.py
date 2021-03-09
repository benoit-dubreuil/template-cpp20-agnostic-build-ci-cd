import argparse
import subprocess
from pathlib import Path
from typing import AnyStr

from compiler_version import CompilerVersion
from data_model import Compiler
from fetch_compiler_version import assure_compiler_path_integrity, fetch_compiler_version


def _fetch_raw_gnu_compiler_version(compiler: Path) -> AnyStr:
    assure_compiler_path_integrity(compiler)

    result: subprocess.CompletedProcess = subprocess.run(
        [compiler, '-dumpversion'], capture_output=True, text=True, check=True
    )

    return result.stdout


def fetch_gnu_compiler_version(compiler: Path) -> CompilerVersion:
    return fetch_compiler_version(compiler, _fetch_raw_gnu_compiler_version)


def cli_fetch_gnu_compiler_version(compiler: Compiler):
    compiler_arg = compiler.value

    arg_parser = argparse.ArgumentParser(description=f'Fetches {compiler.name} compiler\'s version')
    arg_parser.add_argument(compiler_arg, type=Path, nargs='?', const=compiler_arg, default=compiler_arg, help=f'The {compiler.name} compiler\'s executable path')

    args = arg_parser.parse_args()
    compiler_path = getattr(args, compiler_arg)

    print(fetch_gnu_compiler_version(compiler_path), end='')
