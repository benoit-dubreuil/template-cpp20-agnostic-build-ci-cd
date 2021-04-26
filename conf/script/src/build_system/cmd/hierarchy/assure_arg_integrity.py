__all__ = ['find_or_verify_root_dir',
           'find_or_verify_build_dir']

from pathlib import Path
from typing import Optional

from ext.error import *
from .find_root_dir import *
from .find_build_dir import *


def find_or_verify_root_dir(unverified_root_dir: Optional[Path] = None) -> Path:
    if unverified_root_dir is None:
        unverified_root_dir = find_root_dir()
    else:
        if not unverified_root_dir.exists():
            raise RootDirNotFoundError()

    return unverified_root_dir


def find_or_verify_build_dir(unverified_build_dir: Optional[Path] = None) -> Path:
    if unverified_build_dir is None:
        unverified_build_dir = find_build_dir()
    else:
        verify_build_dir(build_dir=unverified_build_dir)

    return unverified_build_dir
