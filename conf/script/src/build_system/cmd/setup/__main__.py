#!/usr/bin/env python3

import build_system.cmd.setup.cli
import utils.cli.main
from build_system import cmd


def main():
    cmd.setup.cli.setup()


utils.cli.main.wrap_main(main)
