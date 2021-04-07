from pathlib import Path
from typing import Optional


def setup_build_system(root_dir: Optional[Path] = None, cli_mode: bool = False):
    from build_system.cmd.setup import setup_steps

    root_dir = setup_steps.get_verified_root_dir(unverified_root_dir=root_dir)
    host_compilers = setup_steps.fetch_host_compilers()
    targets = setup_steps.create_targets_build_dirs(root_dir=root_dir, host_compilers=host_compilers)
    setup_steps.setup_targets(root_dir=root_dir, targets=targets, cli_mode=cli_mode)
