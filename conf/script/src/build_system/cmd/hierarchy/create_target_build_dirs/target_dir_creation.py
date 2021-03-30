from pathlib import Path

import build_system.cmd.hierarchy.consts
import build_system.compiler.installed_instance


def create_target_build_dir(build_dir: Path, target_build_dir_name: str) -> Path:
    target_build_dir = build_dir / target_build_dir_name
    target_build_dir.mkdir(mode=build_system.cmd.hierarchy.consts.BUILD_DIR_PERMISSIONS, exist_ok=True)

    return target_build_dir


def all_target_build_dirs_names_to_dirs(build_dir: Path, all_target_build_dir_names: dict[(build_system.compiler.installed_instance.CompilerInstance, list[str])]) \
        -> dict[(build_system.compiler.installed_instance.CompilerInstance, list[Path])]:
    all_target_build_dirs: dict[(build_system.compiler.installed_instance.CompilerInstance, list[Path])] = {}

    for compiler_instance in all_target_build_dir_names:
        target_build_dirs_for_compiler_instance = []

        for target_build_dir_name in all_target_build_dir_names[compiler_instance]:
            target_build_dir = create_target_build_dir(build_dir, target_build_dir_name)
            target_build_dirs_for_compiler_instance.append(target_build_dir)

        all_target_build_dirs[compiler_instance] = target_build_dirs_for_compiler_instance

    return all_target_build_dirs
