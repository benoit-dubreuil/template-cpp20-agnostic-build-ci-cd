#!/usr/bin/env python3

import build_system.cmd.compiler.host.get_info.location.msvc.cli
import ext.cli.main


def main():
    build_system.cmd.compiler.host.get_info.location.msvc.cli.cli_find_msvc_location()


ext.cli.main.wrap_main(main)
