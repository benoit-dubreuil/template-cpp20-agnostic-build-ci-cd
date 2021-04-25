__all__ = ['create_build_dir']

from pathlib import Path
from typing import Optional

from ext.error import *
from ..assure_arg_integrity import *
from ..consts import *
from ..find_build_dir import *


def create_build_dir(root_dir: Optional[Path] = None) -> Path:
    root_dir = find_or_verify_root_dir(unverified_root_dir=root_dir)
    build_dir = get_build_dir_path(root_dir=root_dir)

    if build_dir.exists():
        if not build_dir.is_dir():
            raise BuildDirNotDirError()
    else:
        build_dir.mkdir(mode=BUILD_DIR_PERMISSIONS, parents=True)

    return build_dir
