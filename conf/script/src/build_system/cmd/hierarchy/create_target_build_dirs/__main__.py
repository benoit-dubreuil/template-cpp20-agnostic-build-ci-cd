#!/usr/bin/env python3

import build_system.cmd.hierarchy.create_target_build_dirs.cli
import utils.cli.main


def main():
    build_system.cmd.hierarchy.create_target_build_dirs.cli.create_target_build_dirs()


utils.cli.main.wrap_main(main)
