#!/usr/bin/env python3

import build_system.cmd.hierarchy.find_build_dir.cli
import utils.cli
from build_system import cmd


def main():
    cmd.hierarchy.find_build_dir.cli.find_build_dir()


utils.cli.wrap_main(main)
