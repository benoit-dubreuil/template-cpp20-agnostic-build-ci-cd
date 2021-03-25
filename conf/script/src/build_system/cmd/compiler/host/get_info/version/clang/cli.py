from pathlib import Path

import build_system.cmd.compiler.host.get_info.version.gnu.cli
import build_system.compiler.family


def fetch_gcc_version() -> None:
    build_system.cmd.compiler.host.get_info.version.gnu.cli.fetch_version(compiler_family=build_system.compiler.family.CompilerFamily.CLANG)
