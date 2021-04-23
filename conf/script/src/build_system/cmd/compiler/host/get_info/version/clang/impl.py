from ..gnu import *
from build_system.compiler import *

from ext.meta_prog.encapsulation import *


@export
def fetch_clang_version() -> CompilerVersion:
    return fetch_gnu_version(CompilerFamily.CLANG.value)
