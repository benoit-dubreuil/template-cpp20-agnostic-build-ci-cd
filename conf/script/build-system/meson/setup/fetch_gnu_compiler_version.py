import argparse
import subprocess
from pathlib import Path

from compiler_version import CompilerVersion
from data_model import Compiler
from fetch_compiler_version import assure_compiler_path_integrity, interpret_fetched_compiler_version


def fetch_gnu_compiler_version(compiler: Path) -> CompilerVersion:
    assure_compiler_path_integrity(compiler)

    result: subprocess.CompletedProcess = subprocess.run(
        [compiler, '-dumpversion'], capture_output=True, text=True, check=True
    )

    return interpret_fetched_compiler_version(result.stdout)


def cli_fetch_gnu_compiler_version(compiler: Compiler):
    compiler_arg = compiler.value

    arg_parser = argparse.ArgumentParser(description=f'Fetches {compiler.name} compiler\'s version')
    arg_parser.add_argument(compiler_arg, type=Path, nargs='?', const=compiler_arg, default=compiler_arg, help=f'The {compiler.name} compiler\'s executable path')

    args = arg_parser.parse_args()
    compiler_path = getattr(args, compiler_arg)

    print(fetch_gnu_compiler_version(compiler_path), end='')
