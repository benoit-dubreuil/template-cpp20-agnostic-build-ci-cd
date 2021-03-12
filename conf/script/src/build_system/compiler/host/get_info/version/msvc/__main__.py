#!/usr/bin/env python3

from src import utils

# Run as a script
if __name__ == '__main__':
    utils.cli.init()
    src.build_system.compiler.host.get_info.version.msvc.cli.fetch_version()
