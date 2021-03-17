#!/usr/bin/env python3

import build_system.compiler.host.get_info.version.gnu.cli
import utils.cli
from build_system.compiler.family import CompilerFamily
from build_system.compiler.host.get_info import version


def main():
    version.gnu.cli.cli_fetch_gnu_compiler_version(CompilerFamily.CLANG)


utils.cli.main.wrap_main(main)
