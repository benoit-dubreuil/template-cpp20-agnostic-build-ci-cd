from pathlib import Path
from typing import Optional, cast

import build_system.cmd.hierarchy.assure_arg_integrity


def _recreate_build_dir(root_dir: Optional[Path] = None) -> Path:
    import build_system.cmd.hierarchy.clean_build_dir
    import build_system.cmd.hierarchy.create_build_dir
    import build_system.cmd.hierarchy.find_build_dir

    build_dir = build_system.cmd.hierarchy.find_build_dir.get_build_dir_path_relative_to_root_dir(root_dir=root_dir)
    build_system.cmd.hierarchy.clean_build_dir.clean_build_dir(build_dir=build_dir, ignore_errors=True)
    build_dir = build_system.cmd.hierarchy.create_build_dir.create_build_dir(root_dir=root_dir)

    return build_dir


def _create_target_build_dirs(root_dir: Optional[Path] = None, supported_installed_compilers=None) -> list[Path]:
    import build_system.cmd.hierarchy.create_target_build_dirs

    root_dir = build_system.cmd.hierarchy.assure_arg_integrity.assure_root_dir_exists(root_dir=root_dir)
    build_dir = _recreate_build_dir(root_dir)
    target_build_dirs = build_system.cmd.hierarchy.create_target_build_dirs.create_target_build_dirs(build_dir=build_dir,
                                                                                                     supported_installed_compilers=supported_installed_compilers)

    return target_build_dirs


def setup_build_system(root_dir: Optional[Path] = None):
    import build_system.compiler.installed_instance
    import build_system.compiler.installed_instance.msvc
    import build_system.compiler.supported_installed_instances

    host_compilers: list[build_system.compiler.installed_instance.CompilerInstance] = build_system.compiler.supported_installed_instances.fetch_all()
    target_build_dirs: list[Path] = _create_target_build_dirs(root_dir=root_dir, supported_installed_compilers=host_compilers)

    # TODO : Execute this inside a 'Visual Studio 2019 Developer Command Prompt' for MSVC
    # Voir C:\Program Files (x86)\Microsoft Visual Studio\2019\BuildTools\VC\Auxiliary\Build
    # %comspec% /k "C:\Program Files (x86)\Microsoft Visual Studio\2019\BuildTools\VC\Auxiliary\Build\vcvars64.bat"
    import subprocess
    import os

    msvc_compiler: build_system.compiler.installed_instance.msvc.MSVCCompilerInstance = cast(build_system.compiler.installed_instance.msvc.MSVCCompilerInstance, host_compilers[0])
    timeout_in_seconds: float = 20

    arg_sep = ' '
    cmd_interpreter = r'cmd'
    cmd_interpreter_option_on_end = r'/c'
    cmd_interpreter_redirect_to_null = arg_sep.join([r'>', os.devnull, r' 2>&1'])
    cmd_arg_vcvars_batch_file = '"' + str(msvc_compiler.vcvars_arch_batch_file) + '"'
    cmd_arg_and = r'&&'
    cmd_arg_get_env_vars = r'set'
    formed_cmd_get_env_var = arg_sep.join([cmd_interpreter,
                                           cmd_interpreter_option_on_end,
                                           cmd_arg_vcvars_batch_file,
                                           cmd_interpreter_redirect_to_null,
                                           cmd_arg_and,
                                           cmd_arg_get_env_vars])

    cmd_get_env_vars_output = subprocess.check_output(formed_cmd_get_env_var, stderr=subprocess.DEVNULL, timeout=timeout_in_seconds)
    cmd_get_env_vars_output = cmd_get_env_vars_output.decode()

    env_vars_post_vcvar: {str: list[str]} = {}

    for env_var in cmd_get_env_vars_output.splitlines():
        env_var_key, env_var_grouped_values = env_var.split(sep='=', maxsplit=1)
        env_var_split_values = env_var_grouped_values.split(sep=';')

        env_vars_post_vcvar[env_var_key] = env_var_split_values

    # TODO : WIP
    import mesonbuild.mesonmain

    current_package_path = Path(__file__).parent
    current_package_path.resolve(strict=True)
    current_package_path = current_package_path.absolute()

    meson_launcher: str = str(current_package_path)
    meson_cli_args: list[str] = ['-h']

    mesonbuild.mesonmain.run(meson_cli_args, meson_launcher)
