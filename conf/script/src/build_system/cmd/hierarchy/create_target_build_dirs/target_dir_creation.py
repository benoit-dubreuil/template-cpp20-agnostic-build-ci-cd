from pathlib import Path

import build_system.build_target.build_target_cls
import build_system.build_target.compiler_instance_targets
import build_system.cmd.hierarchy.consts


def create_all_compiler_instances_target_build_dirs(build_dir: Path,
                                                    all_compiler_instances_targets: list[build_system.build_target.compiler_instance_targets.CompilerInstanceTargets]) -> None:
    for compiler_instance_targets in all_compiler_instances_targets:
        for build_target in compiler_instance_targets:
            create_compiler_instance_target_build_dir(build_dir=build_dir, compiler_instance_target=build_target)


def create_compiler_instance_target_build_dir(build_dir: Path, compiler_instance_target: build_system.build_target.build_target_cls.BuildTarget) -> None:
    compiler_instance_target.compute_target_build_dir(project_build_dir=build_dir)
    compiler_instance_target.dir.mkdir(mode=build_system.cmd.hierarchy.consts.BUILD_DIR_PERMISSIONS, exist_ok=True)
