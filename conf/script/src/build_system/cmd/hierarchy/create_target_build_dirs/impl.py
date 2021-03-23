from pathlib import Path
from typing import Optional

import utils.error.cls_def
import utils.more_path


def create_target_build_dirs(build_dir: Optional[Path] = None) -> list[Path]:
    import build_system.cmd.hierarchy.clean_build_dir
    import build_system.cmd.hierarchy.create_build_dir
    import build_system.cmd.hierarchy.create_target_build_dirs.target_dir_name_generation
    import build_system.cmd.hierarchy.create_target_build_dirs.target_dir_creation

    if build_dir is None:
        build_dir = build_system.cmd.hierarchy.create_build_dir.create_build_dir(root_dir=build_dir)
    else:
        if not build_dir.exists():
            raise utils.error.cls_def.BuildDirNotFoundError()

    if build_dir.exists():
        if not utils.more_path.is_dir_empty(build_dir):
            raise utils.error.cls_def.BuildDirNotEmptyError()

    target_build_dir_names = build_system.cmd.hierarchy.create_target_build_dirs.target_dir_name_generation.generate_target_build_dir_names()

    if len(target_build_dir_names) <= 0:
        raise utils.error.cls_def.NoSupportedCompilersAvailableError()

    return build_system.cmd.hierarchy.create_target_build_dirs.target_dir_creation.create_all_target_build_dirs(build_dir, target_build_dir_names)
