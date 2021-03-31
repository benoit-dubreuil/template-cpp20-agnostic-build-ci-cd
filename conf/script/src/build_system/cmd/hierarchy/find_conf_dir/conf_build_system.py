from pathlib import Path
from typing import Optional

import build_system.cmd.hierarchy.consts
import utils.error.cls_def
import utils.error.try_external_errors


def get_conf_build_system_dir_path_relative_to_conf_dir(conf_dir: Optional[Path] = None) -> Path:
    import build_system.cmd.hierarchy.find_conf_dir.impl

    if conf_dir is None:
        conf_dir = build_system.cmd.hierarchy.find_conf_dir.find_conf_dir()

    return conf_dir / build_system.cmd.hierarchy.consts.CONF_BUILD_SYSTEM_DIR_NAME


def find_conf_build_system_dir(conf_dir: Optional[Path] = None) -> Path:
    conf_build_system_dir = get_conf_build_system_dir_path_relative_to_conf_dir(conf_dir=conf_dir)

    utils.error.try_external_errors.try_manage_strict_path_resolving(path_to_resolve=conf_build_system_dir,
                                                                     external_errors_to_manage={(Exception,): utils.error.cls_def.ConfBuildSystemDirNotFoundError})

    conf_build_system_dir = conf_build_system_dir.absolute()

    if not conf_build_system_dir.is_dir():
        raise utils.error.cls_def.ConfBuildSystemDirNotFoundError()

    return conf_build_system_dir
