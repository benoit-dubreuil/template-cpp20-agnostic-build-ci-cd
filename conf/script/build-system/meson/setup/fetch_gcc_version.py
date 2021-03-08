#!/usr/bin/env python3

import argparse
from pathlib import Path

from data_model import Compiler
from fetch_version_of_gnu_compatible_compiler import fetch_gnu_compiler_version

# Run as a script
if __name__ == '__main__':
    compiler_arg = Compiler.GCC.value

    arg_parser = argparse.ArgumentParser(description='Fetches GCC compiler\'s version')
    arg_parser.add_argument(compiler_arg, type=Path, nargs='?', const=compiler_arg, default=compiler_arg, help='The GCC compiler\'s executable path')

    args = arg_parser.parse_args()
    compiler: Path = getattr(args, compiler_arg)

    print(fetch_gnu_compiler_version(compiler), end='')
