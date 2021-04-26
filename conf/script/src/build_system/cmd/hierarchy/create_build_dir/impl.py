__all__ = ['create_build_dir']

from pathlib import Path
from typing import Optional

from ext.error import *
from ..assure_arg_integrity import *
from ..consts import *
from ..find_build_dir import *


def create_build_dir(root_dir: Optional[Path] = None) -> Path:
    try:
        build_dir = find_build_dir(root_dir=root_dir)
    except BuildDirNotFoundError:
        # PASS INFO TO EXCEPTION!!!!!!
        build_dir.mkdir(mode=BUILD_DIR_PERMISSIONS, parents=True)

    return build_dir
