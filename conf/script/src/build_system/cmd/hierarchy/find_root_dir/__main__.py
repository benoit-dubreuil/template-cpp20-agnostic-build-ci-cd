#!/usr/bin/env python3

import utils.cli
from build_system import cmd
import build_system.cmd.hierarchy.find_root_dir.cli


def main():
    cmd.hierarchy.find_root_dir.cli.find_root_dir()


utils.cli.wrap_main(main)
