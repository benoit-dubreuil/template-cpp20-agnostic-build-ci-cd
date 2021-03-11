#!/usr/bin/env python3

import build_system.compiler.host.get_info.version.msvc.cli

from build_system.compiler.host.get_info import cli
from build_system.compiler.host.get_info import version

# Run as a script
if __name__ == '__main__':
    cli.cli_init()
    version.msvc.cli.fetch_version()
