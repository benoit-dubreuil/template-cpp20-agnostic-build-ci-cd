from pathlib import Path
from typing import Optional

import utils.error.cls_def


def get_verified_root_dir(unverified_root_dir: Optional[Path] = None) -> Path:
    import build_system.cmd.hierarchy.find_root_dir

    if unverified_root_dir is None:
        unverified_root_dir = build_system.cmd.hierarchy.find_root_dir.find_root_dir()
    else:
        if not unverified_root_dir.exists():
            raise utils.error.cls_def.RootDirNotFoundError()

    return unverified_root_dir


def assure_build_dir_exists(build_dir: Optional[Path] = None) -> Path:
    import build_system.cmd.hierarchy.create_build_dir

    if build_dir is None:
        build_dir = build_system.cmd.hierarchy.create_build_dir.create_build_dir()
    else:
        if not build_dir.exists():
            raise utils.error.cls_def.BuildDirNotFoundError()

    return build_dir
