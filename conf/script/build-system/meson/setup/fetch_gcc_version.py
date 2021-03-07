#!/usr/bin/env python3

import subprocess
import argparse
from pathlib import Path

from data_model import Compiler
from compiler_version import CompilerVersion


def fetch_gcc_version(compiler: Path) -> CompilerVersion:
    result: subprocess.CompletedProcess = subprocess.run(
        [compiler, '-dumpversion'], capture_output=True, text=True, check=True
    )

    compiler_version_str: str = result.stdout.strip()
    return CompilerVersion.create_from_str(compiler_version_str)


# Run as a script
if __name__ == '__main__':
    compiler = Compiler.GCC.value

    arg_parser = argparse.ArgumentParser(description='Fetches GCC compiler\'s version')
    arg_parser.add_argument(compiler, type=Path, nargs='?', const=compiler, default=compiler, help='The GCC compiler\'s executable path')

    args = arg_parser.parse_args()
    compiler = args.compiler

    print(fetch_gcc_version(compiler), end='')
