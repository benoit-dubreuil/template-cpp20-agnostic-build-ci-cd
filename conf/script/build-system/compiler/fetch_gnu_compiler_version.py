import subprocess
from pathlib import Path
from typing import AnyStr

from version import CompilerVersion
from fetch_compiler_version import assure_compiler_path_integrity, fetch_compiler_version


def _fetch_raw_gnu_compiler_version(compiler: Path) -> AnyStr:
    assure_compiler_path_integrity(compiler)

    result: subprocess.CompletedProcess = subprocess.run(
        [compiler, '-dumpversion'], capture_output=True, text=True, check=True
    )

    return result.stdout


def fetch_gnu_compiler_version(compiler: Path) -> CompilerVersion:
    return fetch_compiler_version(compiler, _fetch_raw_gnu_compiler_version)
