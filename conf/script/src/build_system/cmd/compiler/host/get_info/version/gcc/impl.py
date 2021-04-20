from build_system.compiler import *
from ..gnu import *

from ext.meta_prog.encapsulation import *


@export
def fetch_gcc_version() -> CompilerVersion:
    return fetch_gnu_version(CompilerFamily.GCC.value)
