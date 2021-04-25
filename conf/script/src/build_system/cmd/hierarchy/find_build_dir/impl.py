__all__ = ['get_build_dir_path',
           'find_build_dir']

from pathlib import Path
from typing import Optional

from ext.error import *
from ext.error.utils import *
from ..consts import *
from ..find_root_dir import *


def get_build_dir_path(root_dir: Optional[Path] = None) -> Path:
    if root_dir is None:
        root_dir = find_root_dir()

    return root_dir / BUILD_DIR_NAME


def find_build_dir(root_dir: Optional[Path] = None) -> Path:
    build_dir = get_build_dir_path(root_dir=root_dir)

    try_manage_strict_path_resolving(path_to_resolve=build_dir,
                                     external_errors_to_manage={(Exception,): BuildDirNotFoundError})

    build_dir = build_dir.absolute()

    if not build_dir.is_dir():
        raise BuildDirNotFoundError()

    return build_dir
