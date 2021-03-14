#!/usr/bin/env python3

import utils.cli
from build_system.cmd.hierarchy.find_root_dir import find_root_dir
from build_system.cmd.hierarchy.find_root_dir import cli


def main():
    root = find_root_dir(cli.get_error_formatted_msg_root_not_found)
    print(root, end=str())


utils.cli.wrap_main(main)
