import colorama
from pathlib import Path

from file_path_integrity import cmd_exists
from compiler_version import CompilerVersion


def cli_init():
    colorama.init()


def assure_compiler_path_integrity(compiler_path: Path):
    """Assures the integrity of the supplied :param:`compiler_path`

    :param compiler_path: The path to the compiler executable file. It must not be a directory.
    """
    if not cmd_exists(str(compiler_path)):
        raise FileNotFoundError('Compiler at the supplied path does not exist or requires ungranted permissions')


def interpret_fetched_compiler_version(compiler_version_str: str) -> CompilerVersion:
    return CompilerVersion.create_from_str(compiler_version_str.strip())
