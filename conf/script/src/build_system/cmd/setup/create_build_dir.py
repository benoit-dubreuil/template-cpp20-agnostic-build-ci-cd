from pathlib import Path
from typing import Final, Optional

import build_system.cmd.hierarchy.find_build_dir
import build_system.cmd.hierarchy.find_root_dir
import utils.error.cls_def

BUILD_DIR_PERMISSIONS: Final[int] = 0o770


def create_build_subdir(build_dir: Path, build_subdir: str):
    build_subdir_path = build_dir / build_subdir
    build_subdir_path.mkdir(mode=BUILD_DIR_PERMISSIONS, exist_ok=True)


def create_all_build_subdirs(build_dir: Path, all_build_subdirs: list[str]):
    for build_subdir in all_build_subdirs:
        create_build_subdir(build_dir, build_subdir)


def find_or_create_build_dir(root_dir: Optional[Path] = None) -> Path:
    if root_dir is None:
        root_dir = build_system.cmd.hierarchy.find_root_dir.find_root_dir()
    else:
        assert root_dir.exists()

    build_dir = build_system.cmd.hierarchy.find_build_dir.find_build_dir_path(root_dir)

    if build_dir.exists():
        if not build_dir.is_dir():
            raise utils.error.cls_def.RootDirNotFoundError()
    else:
        build_dir.mkdir(mode=BUILD_DIR_PERMISSIONS, parents=True)

    return build_dir
