from pathlib import Path
from typing import Optional

import build_system.cmd.hierarchy.consts
import ext.error.core.cls_def
import ext.error.utils.try_external_errors


def get_conf_dir_path_relative_to_root_dir(root_dir: Optional[Path] = None) -> Path:
    import build_system.cmd.hierarchy.find_root_dir

    if root_dir is None:
        root_dir = build_system.cmd.hierarchy.find_root_dir.find_root_dir()

    return root_dir / build_system.cmd.hierarchy.consts.CONF_DIR_NAME


def find_conf_dir(root_dir: Optional[Path] = None) -> Path:
    conf_dir = get_conf_dir_path_relative_to_root_dir(root_dir=root_dir)

    ext.error.utils.try_external_errors.try_manage_strict_path_resolving(path_to_resolve=conf_dir,
                                                                         external_errors_to_manage={(Exception,): ext.error.core.cls_def.ConfDirNotFoundError})

    conf_dir = conf_dir.absolute()

    if not conf_dir.is_dir():
        raise ext.error.core.cls_def.ConfDirNotFoundError()

    return conf_dir
