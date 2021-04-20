from pathlib import Path

from ...cli import *
from .impl import *
from build_system.compiler import *

from ext.meta_prog.encapsulation import *


def cli_fetch_gnu_version(compiler_family: CompilerFamily) -> None:
    fetch_compiler_info_with_default_path(compiler_family=compiler_family,
                                          fetch_compiler_info_func=fetch_gnu_version)
