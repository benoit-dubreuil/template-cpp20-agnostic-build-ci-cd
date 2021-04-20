from pathlib import Path

import build_system.cmd.compiler.host.get_info.version.gnu.cli
import build_system.compiler.core.family


def cli_fetch_gcc_version() -> None:
    build_system.cmd.compiler.host.get_info.version.gnu.cli.cli_fetch_gnu_version(compiler_family=build_system.compiler.core.family.CompilerFamily.GCC)
