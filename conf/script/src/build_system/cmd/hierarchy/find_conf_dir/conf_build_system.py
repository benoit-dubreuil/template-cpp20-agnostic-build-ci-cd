__all__ = ['get_conf_build_system_dir_path_relative_to_conf_dir',
           'find_conf_build_system_dir']

from pathlib import Path
from typing import Optional

from error import *
from error.utils import *
from file_structure import *
from .impl import *


def get_conf_build_system_dir_path_relative_to_conf_dir(conf_dir: Optional[Path] = None) -> Path:
    if conf_dir is None:
        conf_dir = find_conf_dir()

    return conf_dir / CONF_BUILD_SYSTEM_DIR_NAME


def find_conf_build_system_dir(conf_dir: Optional[Path] = None) -> Path:
    conf_build_system_dir = get_conf_build_system_dir_path_relative_to_conf_dir(conf_dir=conf_dir)

    try_manage_strict_path_resolving(path_to_resolve=conf_build_system_dir,
                                     external_errors_to_manage={(Exception,): ConfBuildSystemDirNotFoundError})

    conf_build_system_dir = conf_build_system_dir.absolute()

    if not conf_build_system_dir.is_dir():
        raise ConfBuildSystemDirNotFoundError()

    return conf_build_system_dir
