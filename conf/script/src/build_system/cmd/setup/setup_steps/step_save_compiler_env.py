import os
from pathlib import Path

import javaproperties

import build_system.build_target.build_target
import build_system.build_target.compiler_instance_targets
from build_system.cmd.hierarchy.consts import BUILD_DIR_PERMISSIONS, TARGET_SCRIPT_COMPILER_ENV_NAME, UTF_8


def save_compiler_instances_targets_env(targets: list[build_system.build_target.compiler_instance_targets.CompilerInstanceTargets],
                                        cli_mode: bool) -> None:
    for compiler_instance_targets in targets:
        if compiler_instance_targets.compiler_instance.has_export_shell_env_script():
            for target in compiler_instance_targets:
                _save_compiler_target_env(target=target, cli_mode=cli_mode)


def _save_compiler_target_env(target: build_system.build_target.build_target.BuildTarget,
                              cli_mode: bool) -> None:
    target_compiler_env_file: Path = target.script_dir / TARGET_SCRIPT_COMPILER_ENV_NAME
    target_compiler_env_file.touch(mode=BUILD_DIR_PERMISSIONS, exist_ok=True)

    encoded_env: str = javaproperties.dumps(props= ..., timestamp=False, ensure_ascii=False)
    ...


def _multi_line_compiler_env_to_single_line(compiler_env: [dict[str, list[str]]]) -> [dict[str, str]]:
    single_line_compiler_env: [dict[str, str]] = {}

    for env_key, env_value in compiler_env:
        single_line_env_value: str = os.path.sep.join(env_value)
        single_line_compiler_env[env_key] = single_line_env_value

    return single_line_compiler_env
