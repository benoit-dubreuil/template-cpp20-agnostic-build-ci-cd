#!/usr/bin/env python3

import build_system.cmd.hierarchy.create_targets_build_dirs.cli
import ext.cli.main


def main():
    build_system.cmd.hierarchy.create_targets_build_dirs.cli.cli_create_targets_build_dirs_structure()


ext.cli.main.wrap_main(main)
