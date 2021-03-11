from build_system.compiler.compiler_family import CompilerFamily
from build_system.compiler.host.get_info import cli, version


def cli_fetch_gnu_compiler_version(compiler_family: CompilerFamily):
    cli.cli_fetch_compiler_info_with_default_path(compiler, version.gnu.fetch)
