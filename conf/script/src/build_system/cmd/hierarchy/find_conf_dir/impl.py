__all__ = ['get_conf_dir_path_relative_to_root_dir',
           'find_conf_dir']

from typing import Optional
from pathlib import Path

from ext.error import *
from ext.error.utils import *
from ..consts import *
from ..find_root_dir import *


def get_conf_dir_path_relative_to_root_dir(root_dir: Optional[Path] = None) -> Path:
    if root_dir is None:
        root_dir = find_root_dir()

    return root_dir / CONF_DIR_NAME


def find_conf_dir(root_dir: Optional[Path] = None) -> Path:
    conf_dir = get_conf_dir_path_relative_to_root_dir(root_dir=root_dir)

    try_manage_strict_path_resolving(path_to_resolve=conf_dir,
                                     external_errors_to_manage={(Exception,): ConfDirNotFoundError})

    conf_dir = conf_dir.absolute()

    if not conf_dir.is_dir():
        raise ConfDirNotFoundError()

    return conf_dir
