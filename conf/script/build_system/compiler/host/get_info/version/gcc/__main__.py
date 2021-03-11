#!/usr/bin/env python3
import utils.cli
from build_system.compiler.family import CompilerFamily
from build_system.compiler.host.get_info import version
from build_system.compiler.host.get_info.version import gnu

# Run as a script
if __name__ == '__main__':
    utils.cli.cli_init()
    version.gnu.cli.cli_fetch_gnu_compiler_version(CompilerFamily.GCC)
