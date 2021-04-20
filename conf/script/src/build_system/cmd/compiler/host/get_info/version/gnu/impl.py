import subprocess
from pathlib import Path
from typing import AnyStr

import build_system.cmd.compiler.host.get_info.version.generic_fetch
import build_system.compiler.core.version


def _fetch_raw(compiler: Path) -> AnyStr:
    build_system.cmd.compiler.host.get_info.version.generic_fetch.verify_compiler_path(compiler)

    result: subprocess.CompletedProcess = subprocess.run(
        [compiler, '-dumpversion'], capture_output=True, text=True, check=True
    )

    return result.stdout


def fetch_version(compiler: Path) -> build_system.compiler.core.version.CompilerVersion:
    return build_system.cmd.compiler.host.get_info.version.generic_fetch.fetch_compiler_version(compiler, _fetch_raw)
