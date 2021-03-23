from pathlib import Path
from typing import Optional

import utils.error.cls_def


def setup_build_system(root_dir: Optional[Path] = None):
    import build_system.cmd.hierarchy.clean_build_dir
    import build_system.cmd.hierarchy.create_build_dir
    import build_system.cmd.hierarchy.find_root_dir
    import build_system.cmd.hierarchy.find_build_dir
    import build_system.cmd.hierarchy.create_target_build_dirs.target_dir_name_generation
    import build_system.cmd.setup.create_build_subdirs

    if root_dir is None:
        root_dir = build_system.cmd.hierarchy.find_root_dir.find_root_dir()
    else:
        if not root_dir.exists():
            raise utils.error.cls_def.RootDirNotFoundError()

    build_dir = build_system.cmd.hierarchy.find_build_dir.find_build_dir_path(root_dir=root_dir)
    build_system.cmd.hierarchy.clean_build_dir.clean_build_dir(build_dir=build_dir, ignore_errors=True)
    build_dir = build_system.cmd.hierarchy.create_build_dir.create_build_dir(root_dir=root_dir)

    all_build_subdir_names = build_system.cmd.hierarchy.create_target_build_dirs.target_dir_name_generation.generate_all_build_subdir_names()
    build_system.cmd.setup.create_build_subdirs.create_all_build_subdirs(build_dir, all_build_subdir_names)
