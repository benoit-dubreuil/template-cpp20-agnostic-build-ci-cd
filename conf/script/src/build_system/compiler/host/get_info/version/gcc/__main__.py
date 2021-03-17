#!/usr/bin/env python3

import utils.cli
from build_system.compiler.family import CompilerFamily
from build_system.compiler.host.get_info import version
import build_system.compiler.host.get_info.version.gnu.cli


def main():
    version.gnu.cli.cli_fetch_gnu_compiler_version(CompilerFamily.GCC)


utils.cli.main.wrap_main(main)
