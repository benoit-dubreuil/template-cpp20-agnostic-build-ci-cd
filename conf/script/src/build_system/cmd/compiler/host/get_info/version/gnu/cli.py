import build_system.cmd.compiler.host.get_info.cli
import build_system.compiler.family


def fetch_gnu_compiler_version(compiler_family: build_system.compiler.family.CompilerFamily):
    build_system.cmd.compiler.host.get_info.cli.fetch_compiler_info_with_default_path(compiler_family,
                                                                                      build_system.cmd.compiler.host.get_info.version.gnu.fetch_version)
