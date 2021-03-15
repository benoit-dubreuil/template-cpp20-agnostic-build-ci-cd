import shutil
from pathlib import Path
from typing import Final, NoReturn, Optional

import build_system.cmd.hierarchy.find_root_dir
import utils.cli

BUILD_DIR_NAME: Final[str] = 'build'


def _get_error_msg_build_not_found() -> str:
    return utils.cli.format_error_msg('Build directory not found')


def _error_build_not_found() -> NoReturn:
    raise FileNotFoundError(_get_error_msg_build_not_found())


def find_build_dir(root_dir: Optional[Path] = None) -> Path:
    if root_dir is None:
        root_dir = build_system.cmd.hierarchy.find_root_dir.find_root_dir()

    build_dir = root_dir / BUILD_DIR_NAME

    try:
        build_dir = build_dir.resolve(True)
    except FileNotFoundError:
        _error_build_not_found()

    if not build_dir.is_dir():
        _error_build_not_found()

    return build_dir


def clean_build_dir(root_dir: Optional[Path] = None, ignore_errors=False) -> bool:
    # noinspection PyUnusedLocal
    def _on_rmtree_error(function, path, excinfo):
        nonlocal has_successfuly_cleaned_build
        has_successfuly_cleaned_build = False

    has_successfuly_cleaned_build = True
    build_dir: Optional[Path] = None

    try:
        build_dir = find_build_dir(root_dir)
    except OSError as raised_exception:
        if not ignore_errors:
            raise raised_exception

    if build_dir is not None:
        shutil.rmtree(build_dir, ignore_errors, _on_rmtree_error)

    return (build_dir is not None) and has_successfuly_cleaned_build
