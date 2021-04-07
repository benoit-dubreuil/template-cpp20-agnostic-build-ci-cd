from pathlib import Path

import build_system.build_target.compiler_instance_targets
import build_system.compiler.installed_instance


def create_targets_build_dirs(root_dir: Path,
                              host_compilers: list[build_system.compiler.installed_instance.CompilerInstance]) \
        -> list[build_system.build_target.compiler_instance_targets.CompilerInstanceTargets]:
    from build_system.cmd.hierarchy.create_target_build_dirs import create_target_build_dirs

    build_dir = _recreate_build_dir(root_dir)
    target_build_dirs = create_target_build_dirs(build_dir=build_dir, compiler_instances=host_compilers)

    return target_build_dirs


def _recreate_build_dir(root_dir: Path) -> Path:
    from build_system.cmd.hierarchy.clean_build_dir import clean_build_dir
    from build_system.cmd.hierarchy.create_build_dir import create_build_dir
    from build_system.cmd.hierarchy.find_build_dir import get_build_dir_path_relative_to_root_dir

    build_dir = get_build_dir_path_relative_to_root_dir(root_dir=root_dir)
    clean_build_dir(build_dir=build_dir, ignore_errors=True)
    build_dir = create_build_dir(root_dir=root_dir)

    return build_dir
