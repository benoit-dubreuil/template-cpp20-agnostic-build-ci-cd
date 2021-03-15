import shutil
from pathlib import Path
from typing import Final, Optional

import build_system.cmd.hierarchy.find_root_dir
from build_system import cmd

BUILD_DIR_NAME: Final[str] = 'build'


def find_build_dir(root_dir: Optional[Path] = None) -> Path:
    if root_dir is None:
        root_dir = cmd.hierarchy.find_root_dir.find_root_dir()

    build_dir = root_dir / BUILD_DIR_NAME

    try:
        build_dir = build_dir.resolve(True)
    except FileNotFoundError:
        raise cmd.hierarchy.find_build_dir.error.BuildDirNotFoundError()

    if not build_dir.is_dir():
        raise cmd.hierarchy.find_build_dir.error.BuildDirNotFoundError()

    return build_dir
