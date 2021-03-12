#!/usr/bin/env python3

from src import utils
from build_system.compiler.host.get_info import location

# Run as a script
if __name__ == '__main__':
    utils.cli.init()
    location.msvc.cli.find()
