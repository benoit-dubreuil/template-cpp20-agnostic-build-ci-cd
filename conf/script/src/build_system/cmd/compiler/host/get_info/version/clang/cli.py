from pathlib import Path

from ..gnu import *
from build_system.compiler import *

from ext.meta_prog.encapsulation import *


@export
def cli_fetch_clang_version() -> None:
    cli_fetch_gnu_version(compiler_family=CompilerFamily.CLANG)
