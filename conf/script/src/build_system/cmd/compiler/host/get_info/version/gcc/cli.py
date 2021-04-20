from ..gnu import *
from build_system.compiler import *

from ext.meta_prog.encapsulation import *


@export
def cli_fetch_gcc_version() -> None:
    cli_fetch_gnu_version(compiler_family=CompilerFamily.GCC)
