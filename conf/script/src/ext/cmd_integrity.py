__all__ = ['cmd_exists',
           'get_cmd_path']

import shutil
from pathlib import Path


# From https://stackoverflow.com/a/28909933/2924010
def cmd_exists(cmd) -> bool:
    return shutil.which(cmd) is not None


def get_cmd_path(cmd, dir_path=None) -> (Path, bool):
    cmd_path_str = shutil.which(cmd=cmd, path=dir_path)
    cmd_path = Path(cmd_path_str)
    exists = cmd_path_str is not None

    return cmd_path, exists
