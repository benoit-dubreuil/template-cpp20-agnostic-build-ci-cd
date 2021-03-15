#!/usr/bin/env python3

import build_system.cmd.hierarchy.find_root_dir.cli
import utils.cli
from build_system import cmd


def main():
    cmd.hierarchy.find_root_dir.cli.find_root_dir()


utils.cli.wrap_main(main)
