#!/usr/bin/env python3

import build_system.cmd.hierarchy.create_build_dir.cli
import ext.cli.main


def main():
    build_system.cmd.hierarchy.create_build_dir.cli.create_build_dir()


ext.cli.main.wrap_main(main)
