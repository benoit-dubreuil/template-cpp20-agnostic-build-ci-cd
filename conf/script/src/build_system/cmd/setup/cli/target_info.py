import contextlib
from typing import Final

import build_system.build_target.build_target
import build_system.compiler.installed_instance


# TODO : Refactor
def print_target_info(compiler_instance: build_system.compiler.installed_instance.CompilerInstance,
                      target: build_system.build_target.build_target.BuildTarget,
                      compiler_env_manager: contextlib.AbstractContextManager) -> None:
    from build_system.cmd.setup.cli.colorize import colorize_label, colorize_path, colorize_header_label

    def print_indented_label_and_info(pre_label_indent: str = str(),
                                      post_label_indent: str = str(),
                                      label: str = str(),
                                      info: str = str(),
                                      color_label: bool = True,
                                      color_info: bool = False) -> None:

        if color_label:
            label_colorized = colorize_label(label=label) + ':'
        else:
            label_colorized = label

        if color_info:
            info_colorized = colorize_path(path_info=info)
        else:
            info_colorized = info

        label_formatted = pre_label_indent + label_colorized + post_label_indent
        line = label_formatted + info_colorized

        print(line)

    def print_post_header_labels_and_info(pre_label_indent: str = str(),
                                          post_label_indent: str = str()):
        label_compiler_family_label = r'Compiler family'
        label_compiler_family_info = compiler_instance.compiler_family.value

        label_compiler_version_label = r'Compiler version'
        label_compiler_version_info = str(compiler_instance.version)

        label_compiler_arch_label = r'Compiler architecture'
        label_compiler_arch_info = compiler_instance.arch.arch_to_bit_name()

        label_compiler_installation_path_label = r'Compiler installation path'
        label_compiler_installation_path_info = str(compiler_instance.installation_dir)

        label_env_label = None
        label_env_info = None

        label_build_type_label = r'Build type'
        label_build_type_info = target.target_build_type.value

        # noinspection PyTypeChecker
        if not isinstance(compiler_env_manager, contextlib.nullcontext):
            label_env_label = r'Environment variables'

            # noinspection PyUnresolvedReferences
            compiler_env: dict[str, list[str]] = compiler_env_manager.get_env()

            label_env_info = str(compiler_env)

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
                                      label=label_compiler_arch_label,
                                      info=label_compiler_arch_info)

        print_indented_label_and_info(pre_label_indent=pre_label_indent,
                                      post_label_indent=post_label_indent,
                                      label=label_compiler_installation_path_label,
                                      info=label_compiler_installation_path_info,
                                      color_info=True)

        print_indented_label_and_info(pre_label_indent=pre_label_indent,
                                      post_label_indent=post_label_indent,
                                      label=label_build_type_label,
                                      info=label_build_type_info)

        # noinspection PyTypeChecker
        if not isinstance(compiler_env_manager, contextlib.nullcontext):
            assert label_env_label is not None
            assert label_env_info is not None

            print_indented_label_and_info(pre_label_indent=pre_label_indent,
                                          post_label_indent=post_label_indent,
                                          label=label_env_label,
                                          info=label_env_info,
                                          color_info=True)

    white_space: Final[str] = ' '

    header_label = r'Target'
    header_colorized_label = colorize_header_label(header=header_label)
    post_header_indent = white_space * 6
    header_total_indent = (white_space * len(header_label)) + post_header_indent

    post_label_indent = white_space * 3

    print_indented_label_and_info(post_label_indent=post_header_indent,
                                  label=header_colorized_label,
                                  color_label=False)

    print_post_header_labels_and_info(pre_label_indent=header_total_indent,
                                      post_label_indent=post_label_indent)
