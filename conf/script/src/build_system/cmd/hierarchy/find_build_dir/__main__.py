#!/usr/bin/env python3

import build_system.cmd.hierarchy.find_build_dir.cli
import ext.cli.main


def main():
    build_system.cmd.hierarchy.find_build_dir.cli.find_build_dir()


ext.cli.main.wrap_main(main)
