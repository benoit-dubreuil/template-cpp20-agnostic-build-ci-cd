from pathlib import Path

import build_system.build_target.build_target
import build_system.build_target.compiler_instance_targets
import build_system.cmd.hierarchy.consts


def create_targets_build_dirs(build_dir: Path,
                              targets: list[build_system.build_target.compiler_instance_targets.CompilerInstanceTargets]) -> None:
    for targets_of_compiler_instance in targets:
        for build_target in targets_of_compiler_instance:
            _create_target_build_dir_of_compiler_instance(build_dir=build_dir, target_of_compiler_instance=build_target)


def _create_target_build_dir_of_compiler_instance(build_dir: Path,
                                                  target_of_compiler_instance: build_system.build_target.build_target.BuildTarget) -> None:
    target_of_compiler_instance.compute_target_build_dir(project_build_dir=build_dir)
    target_of_compiler_instance.dir.mkdir(mode=build_system.cmd.hierarchy.consts.BUILD_DIR_PERMISSIONS, exist_ok=True)