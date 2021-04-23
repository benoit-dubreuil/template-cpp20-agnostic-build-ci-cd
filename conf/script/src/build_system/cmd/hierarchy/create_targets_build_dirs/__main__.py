#!/usr/bin/env python3

import build_system.cmd.hierarchy.create_targets_build_dirs.cli
import ext.cli.main


def main():
    build_system.cmd.hierarchy.create_targets_build_dirs.cli.create_target_build_dirs()


ext.cli.main.wrap_main(main)
