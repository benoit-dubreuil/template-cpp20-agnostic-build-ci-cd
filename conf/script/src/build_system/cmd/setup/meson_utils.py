from pathlib import Path
from typing import Final

import colorama
import mesonbuild.mesonmain

import build_system.build_target.build_target_cls
import build_system.compiler.installed_instance


def setup_host_compiler_target_build_dir(root_dir: Path,
                                         host_compiler: build_system.compiler.installed_instance.CompilerInstance,
                                         target_build_dir: build_system.build_target.build_target_cls.BuildTarget):
    # TODO : WIP
    meson_launcher: str = _fetch_meson_launcher()

    cli_kwarg_assignment_op: Final[str] = r'='

    meson_cli_arg_setup_cmd: Final[str] = r'setup'
    meson_cli_arg_help: Final[str] = r'--help'
    meson_cli_arg_build_type: Final[str] = r'--buildtype' + cli_kwarg_assignment_op + target_build_dir.get_build_type().value
    meson_cli_arg_build_dir: Final[str] = str(target_build_dir.dir)
    meson_cli_arg_source_dir: Final[str] = str(root_dir)

    meson_cli_args: list[str] = [meson_cli_arg_setup_cmd,
                                 meson_cli_arg_build_type,
                                 meson_cli_arg_build_dir,
                                 meson_cli_arg_source_dir]

    _print_target_info(host_compiler=host_compiler, target_build_dir=target_build_dir)

    try:
        mesonbuild.mesonmain.run(meson_cli_args, meson_launcher)
    except SystemExit:
        pass


def _fetch_meson_launcher() -> str:
    current_package_path = _fetch_current_package_path()
    return str(current_package_path)


def _print_target_info(host_compiler: build_system.compiler.installed_instance.CompilerInstance,
                       target_build_dir: build_system.build_target.build_target_cls.BuildTarget) -> None:
    def print_indented_label_and_info(pre_label_indent: str = str(),
                                      post_label_indent: str = str(),
                                      label: str = str(),
                                      info: str = str(),
                                      color_label: bool = True,
                                      color_info: bool = False) -> None:
        if color_label:
            label_colored = colorama.Fore.LIGHTCYAN_EX + label + colorama.Style.RESET_ALL + ':'
        else:
            label_colored = label

        if color_info:
            info_colored = colorama.Fore.LIGHTBLACK_EX + info + colorama.Style.RESET_ALL
        else:
            info_colored = info

        label_formatted = pre_label_indent + label_colored + post_label_indent
        line = label_formatted + info_colored

        print(line)

    white_space: Final[str] = ' '

    header_label = r'Target'
    header_colored_label = colorama.Style.BRIGHT + colorama.Fore.LIGHTCYAN_EX + header_label + colorama.Style.RESET_ALL
    post_header_indent = white_space * 6
    header_total_indent = (white_space * len(header_label)) + post_header_indent

    post_sub_header_indent = white_space * 3

    sub_header_compiler_label = r'Compiler'
    sub_header_compiler_info = str(host_compiler.installation_dir)

    print_indented_label_and_info(post_label_indent=post_header_indent,
                                  label=header_colored_label,
                                  color_label=False)

    print_indented_label_and_info(pre_label_indent=header_total_indent,
                                  post_label_indent=post_sub_header_indent,
                                  label=sub_header_compiler_label,
                                  info=sub_header_compiler_info,
                                  color_info=True)


def _fetch_current_package_path() -> Path:
    current_package_path = Path(__file__).parent
    current_package_path.resolve(strict=True)
    current_package_path = current_package_path.absolute()

    return current_package_path
