import build_system.cmd.compiler.host.get_info.cli
import build_system.cmd.compiler.host.get_info.version
import build_system.compiler.family


def cli_fetch_gnu_compiler_version(compiler_family: build_system.compiler.family.CompilerFamily):
    build_system.cmd.compiler.host.get_info.cli.cli_fetch_compiler_info_with_default_path(compiler_family,
                                                                                          build_system.cmd.compiler.host.get_info.version.gnu.fetch)
