from pathlib import Path
from typing import Optional

import build_system.cmd.hierarchy.consts
import build_system.cmd.hierarchy.find_build_dir
import build_system.cmd.hierarchy.find_root_dir
import utils.error.cls_def


def create_build_dir(root_dir: Optional[Path] = None) -> Path:
    if root_dir is None:
        root_dir = build_system.cmd.hierarchy.find_root_dir.find_root_dir()
    else:
        if not root_dir.exists():
            raise utils.error.cls_def.RootDirNotFoundError()

    build_dir = build_system.cmd.hierarchy.find_build_dir.find_build_dir_path(root_dir)

    if build_dir.exists():
        if not build_dir.is_dir():
            raise utils.error.cls_def.BuildDirNotDirError()
    else:
        build_dir.mkdir(mode=build_system.cmd.hierarchy.consts.BUILD_DIR_PERMISSIONS, parents=True)

    return build_dir
