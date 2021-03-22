#!/usr/bin/env python3

import build_system.cmd.clean_build_dir.cli
import utils.cli.main


def main():
    build_system.cmd.clean_build_dir.cli.clean_build_dir()


utils.cli.main.wrap_main(main)
