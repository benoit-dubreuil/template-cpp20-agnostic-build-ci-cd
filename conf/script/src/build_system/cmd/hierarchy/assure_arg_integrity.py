from pathlib import Path
from typing import Optional

import ext.error.core.cls_def


def get_verified_root_dir(unverified_root_dir: Optional[Path] = None) -> Path:
    from build_system.cmd.hierarchy.find_root_dir import find_root_dir

    if unverified_root_dir is None:
        unverified_root_dir = find_root_dir()
    else:
        if not unverified_root_dir.exists():
            raise ext.error.core.cls_def.RootDirNotFoundError()

    return unverified_root_dir


def get_verified_build_dir(unverified_build_dir: Optional[Path] = None) -> Path:
    from build_system.cmd.hierarchy.create_build_dir import create_build_dir

    if unverified_build_dir is None:
        unverified_build_dir = create_build_dir()
    else:
        if not unverified_build_dir.exists():
            raise ext.error.core.cls_def.BuildDirNotFoundError()

    return unverified_build_dir
