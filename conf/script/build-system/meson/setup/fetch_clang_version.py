#!/usr/bin/env python3

import cli_fetch_compiler_version
from data_model import Compiler
from cli_fetch_gnu_compiler_version import cli_fetch_gnu_compiler_version

# Run as a script
if __name__ == '__main__':
    cli_fetch_compiler_version.cli_init()
    cli_fetch_gnu_compiler_version(Compiler.CLANG)
