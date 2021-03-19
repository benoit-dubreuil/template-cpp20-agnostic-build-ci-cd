#!/usr/bin/env python3

import build_system.cmd.compiler.host.get_info.version.gnu.cli
import utils.cli.main
from build_system.compiler.family import CompilerFamily


def main():
    build_system.cmd.compiler.host.get_info.version.gnu.cli.cli_fetch_gnu_compiler_version(CompilerFamily.CLANG)


utils.cli.main.wrap_main(main)
