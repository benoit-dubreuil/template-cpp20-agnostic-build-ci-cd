import subprocess

from pathlib import Path
from typing import AnyStr

from build_system.compiler.version import CompilerVersion
from build_system.compiler.host.get_info import version


def _fetch_raw_gnu_compiler_version(compiler: Path) -> AnyStr:
    version.assure_compiler_path_integrity(compiler)

    result: subprocess.CompletedProcess = subprocess.run(
        [compiler, '-dumpversion'], capture_output=True, text=True, check=True
    )

    return result.stdout


def fetch_gnu_compiler_version(compiler: Path) -> CompilerVersion:
    return version.fetch_compiler_version(compiler, _fetch_raw_gnu_compiler_version)