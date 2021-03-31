#!/usr/bin/env python3

import build_system.cmd.setup.cli
import utils.cli.main


def main():
    build_system.cmd.setup.cli.setup()


utils.cli.main.wrap_main(main)
