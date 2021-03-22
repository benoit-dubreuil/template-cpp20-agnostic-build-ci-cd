#!/usr/bin/env python3

import build_system.cmd.hierarchy.create_build_dir.cli
import utils.cli.main


def main():
    build_system.cmd.hierarchy.create_build_dir.cli.create_build_dir()


utils.cli.main.wrap_main(main)
