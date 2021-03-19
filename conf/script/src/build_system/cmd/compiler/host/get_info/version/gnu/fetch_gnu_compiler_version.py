import subprocess
from pathlib import Path
from typing import AnyStr

import build_system.cmd.compiler.host.get_info.version.compiler
from build_system.compiler.version import CompilerVersion


def _fetch_raw(compiler: Path) -> AnyStr:
    build_system.cmd.compiler.host.get_info.version.compiler.assure_path_integrity(compiler)

    result: subprocess.CompletedProcess = subprocess.run(
        [compiler, '-dumpversion'], capture_output=True, text=True, check=True
    )

    return result.stdout


def fetch(compiler: Path) -> CompilerVersion:
    return build_system.cmd.compiler.host.get_info.version.compiler.fetch(compiler, _fetch_raw)
