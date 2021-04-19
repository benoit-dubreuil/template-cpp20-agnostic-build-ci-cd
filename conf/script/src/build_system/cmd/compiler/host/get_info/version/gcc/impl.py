import build_system.cmd.compiler.host.get_info.version.gnu
import build_system.compiler.core.family
import build_system.compiler.core.version


def fetch_version() -> build_system.compiler.core.version.CompilerVersion:
    return build_system.cmd.compiler.host.get_info.version.gnu.fetch_version(build_system.compiler.core.family.CompilerFamily.GCC.value)
