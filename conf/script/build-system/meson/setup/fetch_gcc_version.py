#!/usr/bin/env python3

import subprocess

from data_model import Compiler
from compiler_version import CompilerVersion


def fetch_gcc_version() -> CompilerVersion:
    result: subprocess.CompletedProcess = subprocess.run(
        [Compiler.GCC.value, '-dumpversion'], capture_output=True, text=True, check=True
    )

    compiler_version_str: str = result.stdout.strip()
    return CompilerVersion.create_from_str(compiler_version_str)


# Run as a script
if __name__ == '__main__':
    print(fetch_gcc_version(), end='')
