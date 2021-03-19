from build_system.cmd.compiler.host.get_info import cli, version
from build_system.compiler.family import CompilerFamily


def cli_fetch_gnu_compiler_version(compiler_family: CompilerFamily):
    cli.cli_fetch_compiler_info_with_default_path(compiler_family, version.gnu.fetch)
