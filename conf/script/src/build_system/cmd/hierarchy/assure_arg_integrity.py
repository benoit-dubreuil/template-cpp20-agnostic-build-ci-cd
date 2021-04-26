__all__ = ['find_or_verify_root_dir']

from pathlib import Path
from typing import Optional

from ext.error import *
from .find_root_dir import *


def find_or_verify_root_dir(unverified_root_dir: Optional[Path] = None) -> Path:
    if unverified_root_dir is None:
        unverified_root_dir = find_root_dir()
    else:
        if not unverified_root_dir.exists():
            raise RootDirNotFoundError()

    return unverified_root_dir
