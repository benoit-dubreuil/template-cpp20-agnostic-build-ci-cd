#!/usr/bin/env python3

import build_system.cmd.hierarchy.find_conf_dir.cli
import ext.cli.main


def main():
    build_system.cmd.hierarchy.find_conf_dir.cli.cli_find_conf_dir()


ext.cli.main.wrap_main(main)
