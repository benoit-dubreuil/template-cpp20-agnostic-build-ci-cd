__all__ = ['get_verified_root_dir',
           'get_verified_build_dir']

from pathlib import Path
from typing import Optional

from ext.error import *
from .create_build_dir import *
from .find_root_dir import *


def get_verified_root_dir(unverified_root_dir: Optional[Path] = None) -> Path:
    if unverified_root_dir is None:
        unverified_root_dir = find_root_dir()
    else:
        if not unverified_root_dir.exists():
            raise RootDirNotFoundError()

    return unverified_root_dir


def get_verified_build_dir(unverified_build_dir: Optional[Path] = None) -> Path:
    if unverified_build_dir is None:
        unverified_build_dir = create_build_dir()
    else:
        if not unverified_build_dir.exists():
            raise BuildDirNotFoundError()

    return unverified_build_dir
