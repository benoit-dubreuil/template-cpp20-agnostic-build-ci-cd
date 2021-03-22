from pathlib import Path
from typing import Optional

import build_system.cmd.setup.build_name
import build_system.cmd.setup.create_build_dir


def setup_build_system(root_dir: Optional[Path] = None):
    build_dir = build_system.cmd.setup.create_build_dir.find_or_create_build_dir(root_dir)

    all_build_subdir_names = build_system.cmd.setup.build_name.generate_all_build_subdir_names()
    # create_all_build_subdirs(build_dir, all_build_subdir_names)

    # TODO : Remove when #58 is done
    print(*all_build_subdir_names, sep='\n', end=str())
