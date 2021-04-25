__all__ = ['find_or_verify_root_dir']

from pathlib import Path
from typing import Optional

from ....hierarchy import *


def get_verified_root_dir(unverified_root_dir: Optional[Path] = None) -> Path:
    return find_or_verify_root_dir(unverified_root_dir=unverified_root_dir)
