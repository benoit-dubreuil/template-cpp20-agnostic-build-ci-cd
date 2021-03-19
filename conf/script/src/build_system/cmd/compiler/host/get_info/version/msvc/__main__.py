#!/usr/bin/env python3

import build_system.cmd.compiler.host.get_info.version.msvc.cli
import utils.cli.main


def main():
    build_system.cmd.compiler.host.get_info.version.msvc.cli.fetch_version()


utils.cli.main.wrap_main(main)
