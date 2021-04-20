#!/usr/bin/env python3

import build_system.cmd.compiler.host.get_info.version.msvc.cli
import ext.cli.main


def main():
    build_system.cmd.compiler.host.get_info.version.msvc.cli.cli_fetch_msvc_version()


ext.cli.main.wrap_main(main)
