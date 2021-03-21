import build_system.cmd.compiler.host.get_info.version.gnu.impl
import build_system.compiler.version
import build_system.compiler.family


def fetch() -> build_system.compiler.version.CompilerVersion:
    return build_system.cmd.compiler.host.get_info.version.gnu.fetch(build_system.compiler.family.CompilerFamily.GCC.value)
