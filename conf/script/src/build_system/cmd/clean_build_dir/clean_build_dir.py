import shutil
from pathlib import Path
from typing import Optional, Callable, Final, NoReturn

import build_system.cmd.hierarchy.find_root_dir

BUILD_DIR_NAME: Final[str] = 'build'


def get_error_msg_build_not_found() -> str:
    return 'Build directory not found'


def _error_build_not_found(get_error_msg: Callable[[], str] = get_error_msg_build_not_found) -> NoReturn:
    raise FileNotFoundError(get_error_msg())


def find_build_dir(root_dir: Optional[Path] = None, get_error_msg: Callable[[], str] = get_error_msg_build_not_found) -> Path:
    if root_dir is None:
        root_dir = build_system.cmd.hierarchy.find_root_dir.find_root_dir()

    build_dir = root_dir / BUILD_DIR_NAME
    build_dir = build_dir.resolve(True)

    if not build_dir.is_dir():
        _error_build_not_found(get_error_msg)

    return build_dir


def clean_build_dir(root_dir: Optional[Path] = None, ignore_errors=False) -> bool:
    has_successfuly_cleaned_build = True
    found_build_dir = False

    try:
        build_dir = find_build_dir(root_dir)
        found_build_dir = True
    except OSError as raised_exception:
        if not ignore_errors:
            raise raised_exception

    # TODO
    def _on_rmtree_error(function: Callable, path: str, excinfo: str):
        nonlocal has_successfuly_cleaned_build
        has_successfuly_cleaned_build = False

    return False  # TODO
