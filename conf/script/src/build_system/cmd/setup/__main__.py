#!/usr/bin/env python3

import build_system.cmd.setup.cli.impl
import utils.cli.main


def main():
    build_system.cmd.setup.cli.impl.setup()


utils.cli.main.wrap_main(main)
