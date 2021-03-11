#!/usr/bin/env python3

import build_system.compiler.host.get_info.version.gnu.cli
from build_system.compiler.compiler_family import CompilerFamily
from build_system.compiler.host.get_info import cli, version

# Run as a script
if __name__ == '__main__':
    cli.cli_init()
    version.gnu.cli.cli_fetch_gnu_compiler_version(CompilerFamily.CLANG)
