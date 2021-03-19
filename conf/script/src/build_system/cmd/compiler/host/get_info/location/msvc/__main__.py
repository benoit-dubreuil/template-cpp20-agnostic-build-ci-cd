#!/usr/bin/env python3

import build_system.cmd.compiler.host.get_info.location.msvc.cli
import utils.cli.main


def main():
    build_system.cmd.compiler.host.get_info.location.msvc.cli.find()


utils.cli.main.wrap_main(main)
