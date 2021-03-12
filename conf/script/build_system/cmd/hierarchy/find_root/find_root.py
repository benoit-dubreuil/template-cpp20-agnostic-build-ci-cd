from pathlib import Path
from typing import Callable, Final, NoReturn

VCS_DIR_NAME: Final[str] = '.git'


def get_error_msg_root_not_found() -> str:
    return 'Root directory not found'


def _error_root_not_found(get_error_msg: Callable[[], str] = get_error_msg_root_not_found) -> NoReturn:
    raise FileNotFoundError(get_error_msg())


def _walk_parent_path(current_path: Path = Path()) -> (Path, Path):
    return current_path.parent, current_path


def find_root(get_error_msg: Callable[[], str] = get_error_msg_root_not_found) -> Path:
    _error_root_not_found(get_error_msg)
