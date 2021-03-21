#!/usr/bin/env python3

import build_system.cmd.compiler.host.get_info.version.gcc
import utils.cli.main


def main():
    build_system.cmd.compiler.host.get_info.version.gcc.fetch()


utils.cli.main.wrap_main(main)
