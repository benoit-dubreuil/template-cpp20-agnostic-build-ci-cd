import subprocess
from pathlib import Path
from typing import AnyStr

from ..generic_fetch import *
from build_system.compiler import *

from ext.meta_prog.encapsulation import *


def _fetch_raw(compiler: Path) -> AnyStr:
    verify_compiler_path(compiler)

    result: subprocess.CompletedProcess = subprocess.run(
        [compiler, '-dumpversion'], capture_output=True, text=True, check=True
    )

    return result.stdout


@export
def fetch_gnu_version(compiler: Path) -> CompilerVersion:
    return fetch_compiler_version(compiler, _fetch_raw)
