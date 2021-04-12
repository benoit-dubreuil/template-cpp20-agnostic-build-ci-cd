from pathlib import Path

import build_system.build_target.build_target
import build_system.build_target.compiler_instance_targets
from build_system.cmd.hierarchy.consts import TARGET_SCRIPT_EXPORT_SHELL_ENV_VARS_NAME


def create_symlinks_to_compilers_export_shell_env_scripts(targets: list[build_system.build_target.compiler_instance_targets.CompilerInstanceTargets],
                                                          cli_mode: bool) -> None:
    for compiler_instance_targets in targets:
        if compiler_instance_targets.compiler_instance.has_export_shell_env_script():
            for target in compiler_instance_targets:
                _create_symlinks_to_compilers_export_shell_env_script(target=target, cli_mode=cli_mode)


def _create_symlinks_to_compilers_export_shell_env_script(target: build_system.build_target.build_target.BuildTarget,
                                                          cli_mode: bool) -> None:
    from build_system.cmd.setup.cli.compiler_shell_env import print_symlink_to_compiler_export_shell_env_script

    export_shell_env_script: Path = target.compiler_instance.get_export_shell_env_script()

    symlink = target.script_dir / TARGET_SCRIPT_EXPORT_SHELL_ENV_VARS_NAME
    symlink.symlink_to(target=export_shell_env_script, target_is_directory=False)

    target.export_shell_env_symlink = symlink

    if cli_mode:
        print_symlink_to_compiler_export_shell_env_script(target=target)
