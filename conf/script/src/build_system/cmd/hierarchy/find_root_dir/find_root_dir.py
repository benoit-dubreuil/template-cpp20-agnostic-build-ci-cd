from pathlib import Path
from typing import Final

from build_system.cmd.hierarchy.find_root_dir.error import RootDirNotFoundError

VCS_DIR_NAME: Final[str] = '.git'


def is_dir_root(root_dir: Path) -> bool:
    assert root_dir.is_dir()

    vcs_dir = root_dir / VCS_DIR_NAME
    return vcs_dir.is_dir()


def _walk_parent_path(current_path: Path = Path()) -> (Path, Path):
    current_path = current_path.resolve(True)
    last_path = current_path

    return current_path.parent, last_path


def find_root_dir() -> Path:
    current_path, last_path = _walk_parent_path()
    is_last_path_root_dir = is_dir_root(last_path)

    while current_path != last_path and not is_last_path_root_dir:
        is_last_path_root_dir = is_dir_root(current_path)
        current_path, last_path = _walk_parent_path(current_path)

    if not is_last_path_root_dir:
        raise RootDirNotFoundError()

    return last_path
