import abc
import contextlib
from dataclasses import dataclass
from pathlib import Path
from typing import NoReturn, Optional, Type, final

import build_system.compiler.build_option.sanitizer
import build_system.compiler.family
import build_system.compiler.version
import host.architecture
import host.os_family
import ext.error.core.cls_def
import ext.error.core.format
import ext.error.utils.try_external_errors


@dataclass(order=True, frozen=True)
class CompilerInstance(metaclass=abc.ABCMeta):
    compiler_family: build_system.compiler.family.CompilerFamily
    os_family: host.os_family.OSFamily
    arch: host.architecture.Architecture
    version: build_system.compiler.version.CompilerVersion
    installation_dir: Path

    def __init__(self,
                 compiler_family: build_system.compiler.family.CompilerFamily,
                 os_family: host.os_family.OSFamily,
                 arch: host.architecture.Architecture,
                 version: build_system.compiler.version.CompilerVersion,
                 installation_dir: Path
                 ):
        self._assert_compiler_family(compiler_family=compiler_family)

        object.__setattr__(self, 'compiler_family', compiler_family)
        object.__setattr__(self, 'os_family', os_family)
        object.__setattr__(self, 'arch', arch)
        object.__setattr__(self, 'version', version)
        object.__setattr__(self, 'installation_dir', installation_dir)

    @classmethod
    @final
    def create_from_installed_compiler(cls,
                                       compiler_family: build_system.compiler.family.CompilerFamily,
                                       os_family: host.os_family.OSFamily,
                                       arch: host.architecture.Architecture,
                                       installation_dir: Optional[Path] = None) -> 'CompilerInstance':
        import build_system.cmd.compiler.host.get_info.version.fetch_by_criteria

        sub_cls_matching_compiler_family: Type[CompilerInstance] = cls.__checked_search_first_sub_cls_matching_compiler_family(compiler_family=compiler_family)

        if installation_dir is None:
            installation_dir = sub_cls_matching_compiler_family._find_installation_dir_by_compiler_family(compiler_family=compiler_family)
        else:
            ext.error.utils.try_external_errors.try_manage_strict_path_resolving(path_to_resolve=installation_dir,
                                                                                 external_errors_to_manage={(Exception,): ext.error.core.cls_def.CompilerNotFoundError})

        version = build_system.cmd.compiler.host.get_info.version.fetch_by_criteria.fetch_by_compiler_family(compiler_family)

        return sub_cls_matching_compiler_family(compiler_family=compiler_family, os_family=os_family, arch=arch, version=version, installation_dir=installation_dir)

    @classmethod
    def __search_first_sub_cls_matching_compiler_family(cls, compiler_family: build_system.compiler.family.CompilerFamily) -> Optional[Type['CompilerInstance']]:

        subclasses: list[Type[CompilerInstance]] = cls.__subclasses__().copy()
        sublcass_matching_compiler_family: Optional[Type[CompilerInstance]] = None

        while subclasses and subclasses:
            concrete_subclass = subclasses.pop(-1)
            sub_subclasses = concrete_subclass.__subclasses__()

            if len(sub_subclasses) <= 0:

                if compiler_family in concrete_subclass.get_supported_compiler_families():
                    sublcass_matching_compiler_family = concrete_subclass

            else:
                subclasses.extend(sub_subclasses)

        return sublcass_matching_compiler_family

    @classmethod
    def __checked_search_first_sub_cls_matching_compiler_family(cls, compiler_family: build_system.compiler.family.CompilerFamily) -> Type['CompilerInstance']:
        sublcass_matching_compiler_family: Optional[Type[CompilerInstance]] = cls.__search_first_sub_cls_matching_compiler_family(compiler_family=compiler_family)

        if sublcass_matching_compiler_family is None:
            error_msg: str = ext.error.core.format.format_error_msg('Comnpiler is not supported')
            raise TypeError(error_msg)

        return sublcass_matching_compiler_family

    @staticmethod
    @abc.abstractmethod
    def get_supported_compiler_families() -> list[build_system.compiler.family.CompilerFamily]:
        raise NotImplementedError()

    @staticmethod
    def get_supported_sanitizers() -> list[build_system.compiler.build_option.sanitizer.CompilerSanitizer]:
        return [build_system.compiler.build_option.sanitizer.CompilerSanitizer.NONE]

    def create_env_context_manager(self) -> contextlib.AbstractContextManager:
        return contextlib.nullcontext()

    @staticmethod
    def has_export_shell_env_script() -> bool:
        return False

    def get_export_shell_env_script(self) -> NoReturn:
        raise NotImplementedError()

    def get_export_shell_env_script_extension(self) -> NoReturn:
        raise NotImplementedError()

    @staticmethod
    @abc.abstractmethod
    def get_c_compiler_name() -> str:
        raise NotImplementedError()

    @staticmethod
    @abc.abstractmethod
    def get_cpp_compiler_name() -> str:
        raise NotImplementedError()

    @classmethod
    @abc.abstractmethod
    def _find_installation_dir_by_compiler_family(cls, compiler_family: build_system.compiler.family.CompilerFamily) -> Path:
        raise NotImplementedError()

    @classmethod
    @final
    def _assert_compiler_family(cls, compiler_family: build_system.compiler.family.CompilerFamily):
        assert compiler_family in cls.get_supported_compiler_families()
