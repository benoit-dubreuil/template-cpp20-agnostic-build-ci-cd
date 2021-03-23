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
