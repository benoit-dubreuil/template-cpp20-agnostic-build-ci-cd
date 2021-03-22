import build_system.cmd.compiler.host.get_info.version.gnu
import build_system.compiler.family
import build_system.compiler.version


def fetch_version() -> build_system.compiler.version.CompilerVersion:
    return build_system.cmd.compiler.host.get_info.version.gnu.fetch_version(build_system.compiler.family.CompilerFamily.CLANG.value)
