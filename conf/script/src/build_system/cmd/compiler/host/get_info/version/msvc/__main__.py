#!/usr/bin/env python3

import build_system.cmd.compiler.host.get_info.version.msvc.cli
import ext.cli.main


def main():
    build_system.cmd.compiler.host.get_info.version.msvc.cli.fetch_version()


ext.cli.main.wrap_main(main)
