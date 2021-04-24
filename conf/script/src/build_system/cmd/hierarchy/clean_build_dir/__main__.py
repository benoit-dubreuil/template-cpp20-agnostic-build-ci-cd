#!/usr/bin/env python3

import build_system.cmd.hierarchy.clean_build_dir.cli
import ext.cli.main


def main():
    build_system.cmd.hierarchy.clean_build_dir.cli.cli_clean_build_dir()


ext.cli.main.wrap_main(main)
