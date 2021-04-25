__all__ = ['create_symlinks_to_compilers_export_shell_env_scripts']

from pathlib import Path

from build_system.build_target import *
from ..cli import *
from ...hierarchy import *


def create_symlinks_to_compilers_export_shell_env_scripts(targets: list[CompilerInstanceTargets],
                                                          cli_mode: bool) -> None:
    for compiler_instance_targets in targets:
        if compiler_instance_targets.compiler_instance.has_export_shell_env_script():
            for target in compiler_instance_targets:
                _create_symlink_to_compiler_export_shell_env_script(target=target, cli_mode=cli_mode)


def _create_symlink_to_compiler_export_shell_env_script(target: BuildTarget,
                                                        cli_mode: bool) -> None:
    export_shell_env_script: Path = target.compiler_instance.get_export_shell_env_script()

    symlink: Path = target.script_dir / TARGET_SCRIPT_EXPORT_SHELL_ENV_NAME
    symlink.symlink_to(target=export_shell_env_script, target_is_directory=False)

    target.export_shell_env_symlink = symlink

    if cli_mode:
        print_symlink_to_compiler_export_shell_env_script(target=target)
