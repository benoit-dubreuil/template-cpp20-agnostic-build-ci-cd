from pathlib import Path

import build_system.build_target.build_target
import build_system.build_target.compiler_instance_targets


def save_compiler_env(targets: list[build_system.build_target.compiler_instance_targets.CompilerInstanceTargets],
                      cli_mode: bool):
    for compiler_instance_targets in targets:
        if compiler_instance_targets.compiler_instance.has_export_shell_env_script():
            for target in compiler_instance_targets:
                ...
