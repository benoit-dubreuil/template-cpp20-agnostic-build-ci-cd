import build_system.build_target.build_target
import build_system.build_target.compiler_instance_targets
from build_system.cmd.hierarchy.consts import BUILD_DIR_PERMISSIONS, TARGET_SCRIPT_DIR_NAME


def create_targets_script_dirs(targets: list[build_system.build_target.compiler_instance_targets.CompilerInstanceTargets]) -> None:
    for targets_of_compiler_instance in targets:
        for build_target in targets_of_compiler_instance:
            _create_target_script_dir_of_compiler_instance(target_of_compiler_instance=build_target)


def _create_target_script_dir_of_compiler_instance(target_of_compiler_instance: build_system.build_target.build_target.BuildTarget) -> None:
    target_of_compiler_instance.script_dir = target_of_compiler_instance.dir / TARGET_SCRIPT_DIR_NAME
    target_of_compiler_instance.script_dir.mkdir(mode=BUILD_DIR_PERMISSIONS, exist_ok=True)