#!/usr/bin/env python3

import build_system.cmd.compiler.host.get_info.location.msvc.cli
import ext.cli.main


def main():
    build_system.cmd.compiler.host.get_info.location.msvc.cli.find()


ext.cli.main.wrap_main(main)
