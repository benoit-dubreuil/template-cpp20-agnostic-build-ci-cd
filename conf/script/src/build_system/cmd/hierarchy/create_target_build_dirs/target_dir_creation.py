from pathlib import Path

import build_system.cmd.hierarchy.consts
import build_system.compiler.installed_instance


def create_target_build_dir(build_dir: Path, target_build_dir_name: str) -> Path:
    target_build_dir = build_dir / target_build_dir_name
    target_build_dir.mkdir(mode=build_system.cmd.hierarchy.consts.BUILD_DIR_PERMISSIONS, exist_ok=True)

    return target_build_dir


def create_all_target_build_dirs(build_dir: Path, all_target_build_dir_names: list[(build_system.compiler.installed_instance.CompilerInstance, str)]) \
        -> dict[(build_system.compiler.installed_instance.CompilerInstance, list[Path])]:
    all_target_build_dirs: list[(Path, build_system.compiler.installed_instance.CompilerInstance)] = []

    for compiler_instance, target_build_dir_name in all_target_build_dir_names:
        target_build_dir = create_target_build_dir(build_dir, target_build_dir_name)
        all_target_build_dirs.append((target_build_dir, compiler_instance))

    return all_target_build_dirs
