__all__ = ['setup_build_system']

from pathlib import Path
from typing import Optional

from .._priv import setup_steps as _step


def setup_build_system(root_dir: Optional[Path] = None, cli_mode: bool = False):
    root_dir = _step.get_verified_root_dir(unverified_root_dir=root_dir)
    host_compilers = _step.fetch_host_compilers()
    targets = _step.create_targets_build_dirs(root_dir=root_dir, compiler_instances=host_compilers)

    _step.setup_targets(root_dir=root_dir, targets=targets, cli_mode=cli_mode)
    _step.create_symlinks_to_compilers_export_shell_env_scripts(targets=targets, cli_mode=cli_mode)
    _step.save_compiler_instances_targets_env(targets=targets, cli_mode=cli_mode)
