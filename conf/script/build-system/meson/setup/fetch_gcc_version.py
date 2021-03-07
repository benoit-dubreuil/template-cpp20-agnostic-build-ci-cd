#!/usr/bin/env python3

import subprocess
import argparse
from pathlib import Path

from data_model import Compiler
from compiler_version import CompilerVersion
from file_path_integrity import assure_file_path_integrity, cmd_exists


def assure_compiler_path_integrity(compiler_path: Path):
    if not cmd_exists(str(compiler_path)):
        raise FileNotFoundError('Compiler at the supplied path does not exist or requires ungranted permissions')


def fetch_gcc_version(compiler: Path) -> CompilerVersion:
    assure_compiler_path_integrity(compiler)

    result: subprocess.CompletedProcess = subprocess.run(
        [compiler, '-dumpversion'], capture_output=True, text=True, check=True
    )

    compiler_version_str: str = result.stdout.strip()
    return CompilerVersion.create_from_str(compiler_version_str)


# Run as a script
if __name__ == '__main__':
    compiler_arg = Compiler.GCC.value

    arg_parser = argparse.ArgumentParser(description='Fetches GCC compiler\'s version')
    arg_parser.add_argument(compiler_arg, type=Path, nargs='?', const=compiler_arg, default=compiler_arg, help='The GCC compiler\'s executable path')

    args = arg_parser.parse_args()
    compiler: Path = getattr(args, compiler_arg)

    print(fetch_gcc_version(compiler), end='')
