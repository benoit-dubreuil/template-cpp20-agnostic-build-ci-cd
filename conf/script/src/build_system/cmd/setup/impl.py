import os
import subprocess
from pathlib import Path
from typing import Final, Optional, cast

import build_system.cmd.hierarchy.assure_arg_integrity
import build_system.compiler.installed_instance
import build_system.compiler.installed_instance.msvc


def _recreate_build_dir(root_dir: Optional[Path] = None) -> Path:
    import build_system.cmd.hierarchy.clean_build_dir
    import build_system.cmd.hierarchy.create_build_dir
    import build_system.cmd.hierarchy.find_build_dir

    build_dir = build_system.cmd.hierarchy.find_build_dir.get_build_dir_path_relative_to_root_dir(root_dir=root_dir)
    build_system.cmd.hierarchy.clean_build_dir.clean_build_dir(build_dir=build_dir, ignore_errors=True)
    build_dir = build_system.cmd.hierarchy.create_build_dir.create_build_dir(root_dir=root_dir)

    return build_dir


def _create_target_build_dirs(root_dir: Optional[Path] = None,
                              supported_installed_compilers: Optional[list[build_system.compiler.installed_instance.compiler_instance]] = None) -> list[Path]:
    import build_system.cmd.hierarchy.create_target_build_dirs

    root_dir = build_system.cmd.hierarchy.assure_arg_integrity.assure_root_dir_exists(root_dir=root_dir)
    build_dir = _recreate_build_dir(root_dir)
    target_build_dirs = build_system.cmd.hierarchy.create_target_build_dirs.create_target_build_dirs(build_dir=build_dir,
                                                                                                     supported_installed_compilers=supported_installed_compilers)

    return target_build_dirs


def setup_build_system(root_dir: Optional[Path] = None):
    import build_system.compiler.supported_installed_instances

    host_compilers: list[build_system.compiler.installed_instance.CompilerInstance] = build_system.compiler.supported_installed_instances.fetch_all()
    host_msvc_compiler = cast(build_system.compiler.installed_instance.msvc.MSVCCompilerInstance, host_compilers[0])
    target_build_dirs: list[Path] = _create_target_build_dirs(root_dir=root_dir, supported_installed_compilers=host_compilers)

    cmd_get_env_vars_output = shell_get_vcvars_env_vars(host_msvc_compiler)

    env_vars_post_vcvars_cmd: {str: list[str]} = {}

    for env_var in cmd_get_env_vars_output.splitlines():
        env_var_key, env_var_grouped_values = env_var.split(sep='=', maxsplit=1)
        env_var_split_values = env_var_grouped_values.split(sep=';')

        env_vars_post_vcvars_cmd[env_var_key] = env_var_split_values

    # TODO : WIP
    import mesonbuild.mesonmain

    current_package_path = Path(__file__).parent
    current_package_path.resolve(strict=True)
    current_package_path = current_package_path.absolute()

    meson_launcher: str = str(current_package_path)
    meson_cli_args: list[str] = ['-h']

    mesonbuild.mesonmain.run(meson_cli_args, meson_launcher)


def shell_get_vcvars_env_vars(host_msvc_compiler: build_system.compiler.installed_instance.msvc.MSVCCompilerInstance) -> str:
    timeout_in_seconds: Final[float] = 20
    arg_sep: Final[str] = ' '
    cmd_interpreter: Final[str] = r'cmd'
    cmd_interpreter_option_on_end: Final[str] = r'/c'
    cmd_interpreter_redirect_to_null: Final[str] = arg_sep.join([r'>', os.devnull, r' 2>&1'])
    cmd_arg_vcvars_batch_file: Final[str] = '"' + str(host_msvc_compiler.vcvars_arch_batch_file) + '"'
    cmd_arg_and: Final[str] = r'&&'
    cmd_arg_get_env_vars: Final[str] = r'set'

    formed_cmd_get_env_var = arg_sep.join([cmd_interpreter,
                                           cmd_interpreter_option_on_end,
                                           cmd_arg_vcvars_batch_file,
                                           cmd_interpreter_redirect_to_null,
                                           cmd_arg_and,
                                           cmd_arg_get_env_vars])

    return subprocess.check_output(formed_cmd_get_env_var, text=True, stderr=subprocess.DEVNULL, timeout=timeout_in_seconds)
