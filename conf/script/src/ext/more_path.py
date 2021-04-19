import pathlib

from .meta_prog.encapsulation import *


@export
def is_dir_empty(dir_path: pathlib.Path) -> bool:
    return not any(dir_path.iterdir())
