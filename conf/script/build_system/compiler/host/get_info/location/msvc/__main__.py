#!/usr/bin/env python3

from build_system.compiler.host.get_info import cli
from build_system.compiler.host.get_info import location
import build_system.compiler.host.get_info.location.msvc.cli

# Run as a script
if __name__ == '__main__':
    cli.cli_init()
    location.msvc.cli.find_installation_path()
