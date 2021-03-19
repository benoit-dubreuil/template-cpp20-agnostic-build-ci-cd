#!/usr/bin/env python3

import utils.cli.main
from build_system.compiler.family import CompilerFamily
import build_system.cmd.compiler.host.get_info.version.gnu.cli


def main():
    build_system.cmd.compiler.host.get_info.version.gnu.cli.cli_fetch_gnu_compiler_version(CompilerFamily.GCC)


utils.cli.main.wrap_main(main)
