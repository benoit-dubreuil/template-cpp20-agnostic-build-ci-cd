#!/usr/bin/env python3

import cli_fetch_compiler_info
from cli_fetch_msvc_version import cli_fetch_msvc_version

# Run as a script
if __name__ == '__main__':
    cli_fetch_compiler_info.cli_init()
    cli_fetch_msvc_version()
