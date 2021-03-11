import subprocess

from pathlib import Path
from typing import AnyStr

from build_system.compiler.version import CompilerVersion
from build_system.compiler.host.get_info import version


def _fetch_raw(compiler: Path) -> AnyStr:
    version.assure_path_integrity(compiler)

    result: subprocess.CompletedProcess = subprocess.run(
        [compiler, '-dumpversion'], capture_output=True, text=True, check=True
    )

    return result.stdout


def fetch(compiler: Path) -> CompilerVersion:
    return version.fetch(compiler, _fetch_raw)
