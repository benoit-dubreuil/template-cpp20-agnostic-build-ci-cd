from pathlib import Path
from typing import Optional

import build_system.cmd.hierarchy.assure_arg_integrity
import build_system.cmd.hierarchy.consts
import build_system.cmd.hierarchy.find_build_dir
import ext.error.core.cls_def


def create_build_dir(root_dir: Optional[Path] = None) -> Path:
    root_dir = build_system.cmd.hierarchy.assure_arg_integrity.get_verified_root_dir(unverified_root_dir=root_dir)
    build_dir = build_system.cmd.hierarchy.find_build_dir.get_build_dir_path_relative_to_root_dir(root_dir=root_dir)

    if build_dir.exists():
        if not build_dir.is_dir():
            raise ext.error.core.cls_def.BuildDirNotDirError()
    else:
        build_dir.mkdir(mode=build_system.cmd.hierarchy.consts.BUILD_DIR_PERMISSIONS, parents=True)

    return build_dir
