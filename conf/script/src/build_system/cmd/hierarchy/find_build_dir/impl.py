from pathlib import Path
from typing import Optional

import build_system.cmd.hierarchy.consts
import utils.error.cls_def
import utils.error.try_external_errors


def get_build_dir_path_relative_to_root_dir(root_dir: Optional[Path] = None) -> Path:
    import build_system.cmd.hierarchy.find_root_dir

    if root_dir is None:
        root_dir = build_system.cmd.hierarchy.find_root_dir.find_root_dir()

    return root_dir / build_system.cmd.hierarchy.consts.BUILD_DIR_NAME


def find_build_dir(root_dir: Optional[Path] = None) -> Path:
    build_dir = get_build_dir_path_relative_to_root_dir(root_dir)

    utils.error.try_external_errors.try_manage_strict_path_resolving(path_to_resolve=build_dir,
                                                                     external_errors_to_manage={(Exception,): utils.error.cls_def.BuildDirNotFoundError})

    build_dir = build_dir.absolute()

    if not build_dir.is_dir():
        raise utils.error.cls_def.BuildDirNotFoundError()

    return build_dir
