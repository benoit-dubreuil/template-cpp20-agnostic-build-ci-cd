__all__ = ['get_root_dir']

from pathlib import Path
from typing import Optional

from ....hierarchy.find_root_dir import *


def get_root_dir(unverified_root_dir: Optional[Path] = None) -> Path:
    return find_or_verify_root_dir(unverified_root_dir=unverified_root_dir)
