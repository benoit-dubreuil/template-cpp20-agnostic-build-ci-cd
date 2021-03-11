#!/usr/bin/env python3

from build_system.compiler.host.get_info.version import gnu
from build_system.compiler.compiler import Compiler
from build_system.compiler.host.get_info import cli
from build_system.compiler.host.get_info import version

# Run as a script
if __name__ == '__main__':
    cli.cli_init()
    version.gnu.cli.cli_fetch_gnu_compiler_version(Compiler.GCC)
