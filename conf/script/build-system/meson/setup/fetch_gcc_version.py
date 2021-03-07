#!/usr/bin/env python3

import subprocess

from data_model import Compiler
import compiler_version


def fetch_gcc_version():
    result: subprocess.CompletedProcess = subprocess.run(
        [Compiler.GCC.value, '-dumpversion'], capture_output=True, text=True, check=True
    )

    print('stdout:', result.stdout.strip(), end='')


# Run as a script
if __name__ == '__main__':
    fetch_gcc_version()
    pass
