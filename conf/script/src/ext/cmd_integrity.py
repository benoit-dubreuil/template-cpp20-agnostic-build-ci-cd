import shutil
from pathlib import Path

from .meta_prog.encapsulation import *


# From https://stackoverflow.com/a/28909933/2924010
@export
def cmd_exists(cmd) -> bool:
    return shutil.which(cmd) is not None


@export
def get_cmd_path(cmd, dir_path=None) -> (Path, bool):
    cmd_path_str = shutil.which(cmd=cmd, path=dir_path)
    cmd_path = Path(cmd_path_str)
    exists = cmd_path_str is not None

    return cmd_path, exists
