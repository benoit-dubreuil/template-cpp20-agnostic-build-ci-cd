#!/usr/bin/env python3

import build_system.cmd.setup.cli.impl
import ext.cli.main


def main():
    build_system.cmd.setup.cli.impl.setup()


ext.cli.main.wrap_main(main)
