from pathlib import Path
from typing import Optional

import utils.error.cls_def
import utils.more_path


def create_target_build_dirs(root_dir: Optional[Path] = None):
    import build_system.cmd.hierarchy.clean_build_dir
    import build_system.cmd.hierarchy.create_build_dir
    import build_system.cmd.hierarchy.find_root_dir
    import build_system.cmd.hierarchy.create_target_build_dirs.target_dir_name_generation
    import build_system.cmd.hierarchy.create_target_build_dirs.target_dir_creation

    if root_dir is None:
        root_dir = build_system.cmd.hierarchy.find_root_dir.find_root_dir()
    else:
        if not root_dir.exists():
            raise utils.error.cls_def.RootDirNotFoundError()

    build_dir = build_system.cmd.hierarchy.create_build_dir.create_build_dir(root_dir=root_dir)

    if build_dir.exists():
        if not utils.more_path.is_dir_empty(build_dir):
            raise utils.error.cls_def.BuildDirNotEmptyError()

    target_build_dir_names = build_system.cmd.hierarchy.create_target_build_dirs.target_dir_name_generation.generate_target_build_dir_names()
    build_system.cmd.hierarchy.create_target_build_dirs.target_dir_creation.create_all_target_build_dirs(build_dir, target_build_dir_names)
