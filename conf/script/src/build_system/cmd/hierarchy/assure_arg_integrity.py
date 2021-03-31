from pathlib import Path
from typing import Optional

import utils.error.cls_def


def assure_root_dir_exists(root_dir: Optional[Path] = None) -> Path:
    import build_system.cmd.hierarchy.find_root_dir

    if root_dir is None:
        root_dir = build_system.cmd.hierarchy.find_root_dir.find_root_dir()
    else:
        if not root_dir.exists():
            raise utils.error.cls_def.RootDirNotFoundError()

    return root_dir


def assure_build_dir_exists(build_dir: Optional[Path] = None) -> Path:
    import build_system.cmd.hierarchy.create_build_dir

    if build_dir is None:
        build_dir = build_system.cmd.hierarchy.create_build_dir.create_build_dir()
    else:
        if not build_dir.exists():
            raise utils.error.cls_def.BuildDirNotFoundError()

    return build_dir
