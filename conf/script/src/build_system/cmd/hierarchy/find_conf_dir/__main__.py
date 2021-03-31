#!/usr/bin/env python3

import build_system.cmd.hierarchy.find_conf_dir.cli
import utils.cli.main


def main():
    build_system.cmd.hierarchy.find_conf_dir.cli.find_conf_dir()


utils.cli.main.wrap_main(main)
