#!/usr/bin/env python3

import build_system.compiler.host.get_info.version.msvc.cli
import utils.cli.main
from build_system.compiler.host.get_info import version


def main():
    version.msvc.cli.fetch_version()


utils.cli.main.wrap_main(main)
