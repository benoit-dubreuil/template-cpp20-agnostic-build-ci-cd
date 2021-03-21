import build_system.cmd.compiler.host.get_info.version.gnu.fetch_gnu_compiler_version
import build_system.compiler.family
import build_system.compiler.version


def fetch() -> build_system.compiler.version.CompilerVersion:
    return build_system.cmd.compiler.host.get_info.version.gnu.fetch(build_system.compiler.family.CompilerFamily.clang.value)
