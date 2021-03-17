#!/usr/bin/env python3

import build_system.cmd.clean_build_dir.cli
import utils.cli
from build_system import cmd


def main():
    cmd.clean_build_dir.cli.clean_build_dir()


utils.cli.cli.wrap_main(main)
