from pathlib import Path
from typing import Optional

import build_system.cmd.clean_build_dir
import build_system.cmd.hierarchy.create_build_dir
import build_system.cmd.hierarchy.find_root_dir


def setup_build_system(root_dir: Optional[Path] = None):
    import build_system.cmd.setup.build_name
    import build_system.cmd.setup.create_build_subdirs

    if root_dir is None:
        root_dir = build_system.cmd.hierarchy.find_root_dir.find_root_dir()
    else:
        assert root_dir.exists()

    build_system.cmd.clean_build_dir.clean_build_dir(root_dir=root_dir, ignore_errors=True)
    build_dir = build_system.cmd.hierarchy.create_build_dir.create_build_dir(root_dir)

    all_build_subdir_names = build_system.cmd.setup.build_name.generate_all_build_subdir_names()
    build_system.cmd.setup.create_build_subdirs.create_all_build_subdirs(build_dir, all_build_subdir_names)
