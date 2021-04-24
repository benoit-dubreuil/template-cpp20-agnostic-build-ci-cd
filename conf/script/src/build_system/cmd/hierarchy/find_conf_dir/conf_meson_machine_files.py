__all__ = ['get_meson_machine_files_dir_path_relative_to_build_system_dir',
           'find_meson_machine_files_dir']

from pathlib import Path
from typing import Optional

from ext.error import *
from ext.error.utils import *
from .conf_build_system import *
from ..consts import *


def get_meson_machine_files_dir_path_relative_to_build_system_dir(conf_build_system_dir: Optional[Path] = None) -> Path:
    if conf_build_system_dir is None:
        conf_build_system_dir = find_conf_build_system_dir()

    return conf_build_system_dir / MESON_MACHINE_FILES_DIR_NAME


def find_meson_machine_files_dir(conf_build_system_dir: Optional[Path] = None) -> Path:
    meson_machine_files_dir = get_meson_machine_files_dir_path_relative_to_build_system_dir(conf_build_system_dir=conf_build_system_dir)

    try_manage_strict_path_resolving(path_to_resolve=meson_machine_files_dir,
                                     external_errors_to_manage={(Exception,): MesonMachineFilesDirNotFoundError})

    meson_machine_files_dir = meson_machine_files_dir.absolute()

    if not meson_machine_files_dir.is_dir():
        raise ConfBuildSystemDirNotFoundError()

    return meson_machine_files_dir
