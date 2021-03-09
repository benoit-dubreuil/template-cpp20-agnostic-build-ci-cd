import argparse
import subprocess
from pathlib import Path

from compiler_version import CompilerVersion
from data_model import Compiler
from file_path_integrity import cmd_exists


def assure_compiler_path_integrity(compiler_path: Path):
    """Assures the integrity of the supplied :param:`compiler_path`

    :param compiler_path: The path to the compiler executable file. It must not be a directory.
    """
    if not cmd_exists(str(compiler_path)):
        raise FileNotFoundError('Compiler at the supplied path does not exist or requires ungranted permissions')


def fetch_gnu_compiler_version(compiler: Path) -> CompilerVersion:
    assure_compiler_path_integrity(compiler)

    result: subprocess.CompletedProcess = subprocess.run(
        [compiler, '-dumpversion'], capture_output=True, text=True, check=True
    )

    compiler_version_str: str = result.stdout.strip()
    return CompilerVersion.create_from_str(compiler_version_str)


def cli_fetch_gnu_compiler_version(compiler: Compiler):
    compiler_arg = compiler.value

    arg_parser = argparse.ArgumentParser(description=f'Fetches {compiler.name} compiler\'s version')
    arg_parser.add_argument(compiler_arg, type=Path, nargs='?', const=compiler_arg, default=compiler_arg, help=f'The {compiler.name} compiler\'s executable path')

    args = arg_parser.parse_args()
    compiler_path = getattr(args, compiler_arg)

    print(fetch_gnu_compiler_version(compiler_path), end='')
