import shutil
from pathlib import Path
from typing import Optional

import build_system.cmd.hierarchy.consts
import build_system.cmd.hierarchy.find_root_dir
import utils.error.cls_def


def find_build_dir_path(root_dir: Optional[Path] = None) -> Path:
    if root_dir is None:
        root_dir = build_system.cmd.hierarchy.find_root_dir.find_root_dir()

    return root_dir / build_system.cmd.hierarchy.consts.BUILD_DIR_NAME


def find_build_dir(root_dir: Optional[Path] = None) -> Path:
    build_dir = find_build_dir_path(root_dir)

    try:
        build_dir = build_dir.resolve(True)
    except FileNotFoundError:
        raise utils.error.cls_def.BuildDirNotFoundError()

    if not build_dir.is_dir():
        raise utils.error.cls_def.BuildDirNotFoundError()

    return build_dir
