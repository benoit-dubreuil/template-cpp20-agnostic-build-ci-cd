#!/usr/bin/env python3

import build_system.cmd.setup.cli.cli_impl
import utils.cli.main


def main():
    build_system.cmd.setup.cli.cli_impl.setup()


utils.cli.main.wrap_main(main)
