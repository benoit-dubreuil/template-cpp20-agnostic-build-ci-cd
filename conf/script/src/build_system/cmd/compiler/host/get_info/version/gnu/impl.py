import subprocess
from pathlib import Path
from typing import AnyStr

import build_system.cmd.compiler.host.get_info.version.generic_fetch
import build_system.compiler.version


def _fetch_raw(compiler: Path) -> AnyStr:
    build_system.cmd.compiler.host.get_info.version.generic_fetch.assure_path_integrity(compiler)

    result: subprocess.CompletedProcess = subprocess.run(
        [compiler, '-dumpversion'], capture_output=True, text=True, check=True
    )

    return result.stdout


def fetch(compiler: Path) -> build_system.compiler.version.CompilerVersion:
    return build_system.cmd.compiler.host.get_info.version.generic_fetch.fetch(compiler, _fetch_raw)
