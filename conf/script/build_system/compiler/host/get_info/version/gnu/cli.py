from build_system.compiler.compiler import Compiler

from build_system.compiler.host.get_info import cli

from build_system.compiler.host.get_info.version import gnu
import build_system.compiler.host.get_info.version.gnu.fetch_gnu_compiler_version


def cli_fetch_gnu_compiler_version(compiler: Compiler):
    cli.cli_fetch_compiler_info_with_default_path(compiler, gnu.fetch.fetch_compiler_version)
