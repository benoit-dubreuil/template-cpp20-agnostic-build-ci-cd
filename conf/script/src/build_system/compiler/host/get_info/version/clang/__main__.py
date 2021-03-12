#!/usr/bin/env python3

from src import utils
from build_system.compiler.family import CompilerFamily
from build_system.compiler.host.get_info import version

# Run as a script
if __name__ == '__main__':
    utils.cli.init()
    version.gnu.cli.cli_fetch_gnu_compiler_version(CompilerFamily.CLANG)
