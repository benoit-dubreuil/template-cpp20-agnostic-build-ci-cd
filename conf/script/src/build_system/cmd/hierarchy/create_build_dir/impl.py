__all__ = ['create_build_dir']

from pathlib import Path
from typing import Optional

from error import *
from file_structure import *
from ..find_build_dir import *


def create_build_dir(root_dir: Optional[Path] = None) -> Path:
    build_dir = get_build_dir_path(root_dir=root_dir)

    try:
        verify_build_dir(build_dir=build_dir)
    except BuildDirNotFoundError:
        build_dir.mkdir(mode=BUILD_DIR_PERMISSIONS, parents=True)

    return build_dir
