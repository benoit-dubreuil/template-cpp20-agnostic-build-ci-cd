from pathlib import Path
from typing import Optional


def get_verified_root_dir(unverified_root_dir: Optional[Path] = None):
    import build_system.cmd.hierarchy.assure_arg_integrity

    verified_root_dir = build_system.cmd.hierarchy.assure_arg_integrity.get_verified_root_dir(unverified_root_dir=unverified_root_dir)
    return verified_root_dir
