from pathlib import Path

import build_system.build_target.build_target
import build_system.build_target.compiler_instance_targets
from build_system.cmd.hierarchy.consts import TARGET_SCRIPT_EXPORT_SHELL_ENV_VARS_NAME


def create_symlinks_to_compilers_export_shell_env_vars_script(targets: list[build_system.build_target.compiler_instance_targets.CompilerInstanceTargets],
                                                              cli_mode: bool):
    for compiler_instance_targets in targets:
        if compiler_instance_targets.compiler_instance.has_export_shell_env_vars_script():
            for target in compiler_instance_targets:
                _create_symlinks_to_compilers_export_shell_env_vars__script(target=target, cli_mode=cli_mode)


def _create_symlinks_to_compilers_export_shell_env_vars__script(target: build_system.build_target.build_target.BuildTarget,
                                                                cli_mode: bool):
    from build_system.cmd.setup.cli_print_symlink_to_compiler_export_shell_env_vars import print_symlink_to_compiler_export_shell_env_vars_script

    export_shell_env_vars_script: Path = target.compiler_instance.get_export_shell_env_vars_script()

    symlink = target.script_dir / TARGET_SCRIPT_EXPORT_SHELL_ENV_VARS_NAME
    symlink.symlink_to(target=export_shell_env_vars_script, target_is_directory=False)

    target.export_shell_env_vars_symlink = symlink

    if cli_mode:
        print_symlink_to_compiler_export_shell_env_vars_script(target=target)
