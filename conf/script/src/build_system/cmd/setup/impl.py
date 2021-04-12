from pathlib import Path
from typing import Optional


def setup_build_system(root_dir: Optional[Path] = None, cli_mode: bool = False):
    from build_system.cmd.setup import setup_steps as step

    root_dir = step.get_verified_root_dir(unverified_root_dir=root_dir)
    host_compilers = step.fetch_host_compilers()
    targets = step.create_targets_build_dirs(root_dir=root_dir, compiler_instances=host_compilers)

    step.setup_targets(root_dir=root_dir, targets=targets, cli_mode=cli_mode)
    step.create_symlinks_to_compilers_export_shell_env_scripts(targets=targets, cli_mode=cli_mode)
    step.save_compiler_instances_targets_env(targets=targets, cli_mode=cli_mode)
