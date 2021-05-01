__all__ = ['get_build_dir_path',
           'verify_build_dir',
           'find_build_dir',
           'find_or_verify_build_dir']

from pathlib import Path
from typing import Optional

from error import *
from error.utils import *
from file_structure import *
from ..find_root_dir import *


def get_build_dir_path(root_dir: Optional[Path] = None) -> Path:
    if root_dir is None:
        root_dir = find_root_dir()

    return root_dir / BUILD_DIR_NAME


def verify_build_dir(build_dir: Path) -> None:
    try_manage_strict_path_resolving(path_to_resolve=build_dir,
                                     external_errors_to_manage={(Exception,): BuildDirNotFoundError})

    if not build_dir.is_dir():
        raise BuildDirNotDirError()


def find_build_dir(root_dir: Optional[Path] = None) -> Path:
    build_dir = get_build_dir_path(root_dir=root_dir)
    verify_build_dir(build_dir=build_dir)

    return build_dir


def find_or_verify_build_dir(unverified_build_dir: Optional[Path] = None) -> Path:
    build_dir: Path

    if unverified_build_dir is None:
        build_dir = find_build_dir()
    else:
        verify_build_dir(build_dir=unverified_build_dir)
        build_dir = unverified_build_dir

    return build_dir
