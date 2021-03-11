#!/usr/bin/env python3

import build_system.compiler.host.get_info.location.msvc.cli
import utils.cli
from build_system.compiler.host.get_info import location

# Run as a script
if __name__ == '__main__':
    utils.cli.cli_init()
    location.msvc.cli.find()
