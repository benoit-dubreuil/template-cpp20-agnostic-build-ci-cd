import colorama
from pathlib import Path
from file_path_integrity import cmd_exists


def cli_init():
    colorama.init()


def assure_compiler_path_integrity(compiler_path: Path):
    """Assures the integrity of the supplied :param:`compiler_path`

    :param compiler_path: The path to the compiler executable file. It must not be a directory.
    """
    if not cmd_exists(str(compiler_path)):
        raise FileNotFoundError('Compiler at the supplied path does not exist or requires ungranted permissions')
