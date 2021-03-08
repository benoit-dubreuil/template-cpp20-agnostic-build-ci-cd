#!/usr/bin/env python3

from data_model import Compiler
from fetch_version_of_gnu_compatible_compiler import cli_fetch_gnu_compiler_version

# Run as a script
if __name__ == '__main__':
    cli_fetch_gnu_compiler_version(Compiler.GCC)
