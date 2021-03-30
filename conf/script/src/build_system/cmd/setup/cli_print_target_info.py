from typing import Final

import colorama

import build_system.build_target.build_target_cls
import build_system.compiler.installed_instance


def print_target_info(host_compiler: build_system.compiler.installed_instance.CompilerInstance,
                      target_build_dir: build_system.build_target.build_target_cls.BuildTarget) -> None:
    def print_indented_label_and_info(pre_label_indent: str = str(),
                                      post_label_indent: str = str(),
                                      label: str = str(),
                                      info: str = str(),
                                      color_label: bool = True,
                                      color_info: bool = False) -> None:
        if color_label:
            label_colored = colorama.Fore.CYAN + label + colorama.Style.RESET_ALL + ':'
        else:
            label_colored = label

        if color_info:
            info_colored = colorama.Fore.LIGHTBLACK_EX + info + colorama.Style.RESET_ALL
        else:
            info_colored = info

        label_formatted = pre_label_indent + label_colored + post_label_indent
        line = label_formatted + info_colored

        print(line)

    def print_post_header_labels_and_info(pre_label_indent: str = str(),
                                          post_label_indent: str = str()):
        label_compiler_family_label = r'Compiler family'
        label_compiler_family_info = host_compiler.compiler_family.value

        label_compiler_version_label = r'Compiler version'
        label_compiler_version_info = str(host_compiler.version)

        label_compiler_installation_path_label = r'Compiler installation path'
        label_compiler_installation_path_info = str(host_compiler.installation_dir)

        label_build_type_label = r'Build type'
        label_build_type_info = target_build_dir.get_build_type().value

        print_indented_label_and_info(pre_label_indent=pre_label_indent,
                                      post_label_indent=post_label_indent,
                                      label=label_compiler_family_label,
                                      info=label_compiler_family_info)

        print_indented_label_and_info(pre_label_indent=pre_label_indent,
                                      post_label_indent=post_label_indent,
                                      label=label_compiler_version_label,
                                      info=label_compiler_version_info)

        print_indented_label_and_info(pre_label_indent=pre_label_indent,
                                      post_label_indent=post_label_indent,
                                      label=label_compiler_installation_path_label,
                                      info=label_compiler_installation_path_info,
                                      color_info=True)

        print_indented_label_and_info(pre_label_indent=pre_label_indent,
                                      post_label_indent=post_label_indent,
                                      label=label_build_type_label,
                                      info=label_build_type_info)

    white_space: Final[str] = ' '

    header_label = r'Target'
    header_colored_label = colorama.Fore.LIGHTCYAN_EX + header_label + colorama.Style.RESET_ALL
    post_header_indent = white_space * 6
    header_total_indent = (white_space * len(header_label)) + post_header_indent

    post_label_indent = white_space * 3

    print_indented_label_and_info(post_label_indent=post_header_indent,
                                  label=header_colored_label,
                                  color_label=False)

    print_post_header_labels_and_info(pre_label_indent=header_total_indent,
                                      post_label_indent=post_label_indent)
