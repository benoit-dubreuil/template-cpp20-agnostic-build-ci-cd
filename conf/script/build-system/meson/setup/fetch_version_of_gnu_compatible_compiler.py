#!/usr/bin/env python3

import subprocess
from pathlib import Path

from compiler_version import CompilerVersion
from file_path_integrity import cmd_exists


def assure_compiler_path_integrity(compiler_path: Path):
    if not cmd_exists(str(compiler_path)):
        raise FileNotFoundError('Compiler at the supplied path does not exist or requires ungranted permissions')


def fetch_gnu_compiler_version(compiler: Path) -> CompilerVersion:
    assure_compiler_path_integrity(compiler)

    result: subprocess.CompletedProcess = subprocess.run(
        [compiler, '-dumpversion'], capture_output=True, text=True, check=True
    )

    compiler_version_str: str = result.stdout.strip()
    return CompilerVersion.create_from_str(compiler_version_str)
