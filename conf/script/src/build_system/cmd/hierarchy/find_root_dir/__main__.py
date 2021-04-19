#!/usr/bin/env python3

import build_system.cmd.hierarchy.find_root_dir.cli
import ext.cli.main


def main():
    build_system.cmd.hierarchy.find_root_dir.cli.find_root_dir()


ext.cli.main.wrap_main(main)
