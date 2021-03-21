#!/usr/bin/env python3

import build_system.cmd.hierarchy.find_root_dir.cli
import utils.cli.main


def main():
    build_system.cmd.hierarchy.find_root_dir.cli.find_root_dir()


utils.cli.main.wrap_main(main)
