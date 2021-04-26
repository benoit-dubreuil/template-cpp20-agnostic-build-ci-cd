__all__ = ['is_dir_empty']

from pathlib import Path


def is_dir_empty(dir_path: Path) -> bool:
    return not any(dir_path.iterdir())
