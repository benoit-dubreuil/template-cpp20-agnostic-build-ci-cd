__all__ = ['create_targets_build_dirs']

from pathlib import Path

from build_system.build_target import *
from build_system.compiler import *
from ...hierarchy import *


def create_targets_build_dirs(root_dir: Path,
                              compiler_instances: list[CompilerInstance]) \
        -> list[CompilerInstanceTargets]:
    build_dir = _recreate_build_dir(root_dir)
    target_build_dirs = create_targets_build_dirs_structure(build_dir=build_dir, compiler_instances=compiler_instances)

    return target_build_dirs


def _recreate_build_dir(root_dir: Path) -> Path:
    build_dir = get_build_dir_path_relative_to_root_dir(root_dir=root_dir)
    clean_build_dir(build_dir=build_dir, ignore_errors=True)
    build_dir = create_build_dir(root_dir=root_dir)

    return build_dir
