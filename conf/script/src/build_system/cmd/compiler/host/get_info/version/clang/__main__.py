#!/usr/bin/env python3

import build_system.cmd.compiler.host.get_info.version.clang.cli
import ext.cli.main


def main():
    build_system.cmd.compiler.host.get_info.version.clang.cli.cli_fetch_clang_version()


ext.cli.main.wrap_main(main)
