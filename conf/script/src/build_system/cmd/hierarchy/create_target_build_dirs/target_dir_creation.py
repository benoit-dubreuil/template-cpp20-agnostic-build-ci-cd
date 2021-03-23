from pathlib import Path

import build_system.cmd.hierarchy.consts


def create_target_build_dir(build_dir: Path, build_subdir: str):
    build_subdir_path = build_dir / build_subdir
    build_subdir_path.mkdir(mode=build_system.cmd.hierarchy.consts.BUILD_DIR_PERMISSIONS, exist_ok=True)


def create_all_target_build_dirs(build_dir: Path, all_build_subdirs: list[str]):
    for build_subdir in all_build_subdirs:
        create_target_build_dir(build_dir, build_subdir)
