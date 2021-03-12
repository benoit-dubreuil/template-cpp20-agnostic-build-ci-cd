from pathlib import Path
from typing import Callable, Final, NoReturn

VCS_DIR_NAME: Final[str] = '.git'


def get_error_msg_root_not_found() -> str:
    return 'Root directory not found'


def is_dir_root(root_dir: Path) -> bool:
    assert root_dir.is_dir()

    vcs_dir = root_dir / VCS_DIR_NAME
    return vcs_dir.is_dir()


def _error_root_not_found(get_error_msg: Callable[[], str] = get_error_msg_root_not_found) -> NoReturn:
    raise FileNotFoundError(get_error_msg())


def _walk_parent_path(current_path: Path = Path()) -> (Path, Path):
    current_path = current_path.resolve(True)
    last_path = current_path

    return current_path.parent, last_path


def find_root(get_error_msg: Callable[[], str] = get_error_msg_root_not_found) -> Path:
    _error_root_not_found(get_error_msg)
