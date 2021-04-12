from pathlib import Path

import build_system.build_target.build_target
import build_system.build_target.compiler_instance_targets
from build_system.cmd.hierarchy.consts import TARGET_SCRIPT_COMPILER_ENV_NAME, BUILD_DIR_PERMISSIONS


def save_compiler_instances_targets_env(targets: list[build_system.build_target.compiler_instance_targets.CompilerInstanceTargets],
                                        cli_mode: bool) -> None:
    for compiler_instance_targets in targets:
        if compiler_instance_targets.compiler_instance.has_export_shell_env_script():
            for target in compiler_instance_targets:
                _save_compiler_target_env(target=target, cli_mode=cli_mode)


def _save_compiler_target_env(target: build_system.build_target.build_target.BuildTarget,
                              cli_mode: bool) -> None:
    target_compiler_env: Path = target.script_dir / TARGET_SCRIPT_COMPILER_ENV_NAME
    target_compiler_env.touch(mode=BUILD_DIR_PERMISSIONS, exist_ok=True)
    ...
