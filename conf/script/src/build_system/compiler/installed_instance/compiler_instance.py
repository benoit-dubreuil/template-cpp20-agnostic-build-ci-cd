__all__ = ['CompilerInstance']

from abc import ABCMeta, abstractmethod
import contextlib
from dataclasses import dataclass
from pathlib import Path
from typing import NoReturn, Optional, Type, final

from ..core import *
from ..build_option import *
from host import *
from ext.error import *
from ext.error.utils import *


@dataclass(order=True, frozen=True)
class CompilerInstance(metaclass=ABCMeta):
    compiler_family: CompilerFamily
    os_family: OSFamily
    arch: Architecture
    version: CompilerVersion
    installation_dir: Path

    def __init__(self,
                 compiler_family: CompilerFamily,
                 os_family: OSFamily,
                 arch: Architecture,
                 version: CompilerVersion,
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
                                       compiler_family: CompilerFamily,
                                       os_family: OSFamily,
                                       arch: Architecture,
                                       installation_dir: Optional[Path] = None) -> 'CompilerInstance':
        import build_system.cmd.compiler.host.get_info.version.fetch_by_criteria

        sub_cls_matching_compiler_family: Type[CompilerInstance] = cls.__checked_search_first_sub_cls_matching_compiler_family(compiler_family=compiler_family)

        if installation_dir is None:
            installation_dir = sub_cls_matching_compiler_family._find_installation_dir_by_compiler_family(compiler_family=compiler_family)
        else:
            try_manage_strict_path_resolving(path_to_resolve=installation_dir,
                                             external_errors_to_manage={(Exception,): CompilerNotFoundError})

        version = build_system.cmd.compiler.host.get_info.version.fetch_by_criteria.fetch_compiler_version_by_family(compiler_family)

        return sub_cls_matching_compiler_family(compiler_family=compiler_family, os_family=os_family, arch=arch, version=version, installation_dir=installation_dir)

    @classmethod
    def __search_first_sub_cls_matching_compiler_family(cls, compiler_family: CompilerFamily) -> Optional[Type['CompilerInstance']]:

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
    def __checked_search_first_sub_cls_matching_compiler_family(cls, compiler_family: CompilerFamily) -> Type['CompilerInstance']:
        sublcass_matching_compiler_family: Optional[Type[CompilerInstance]] = cls.__search_first_sub_cls_matching_compiler_family(compiler_family=compiler_family)

        if sublcass_matching_compiler_family is None:
            error_msg: str = format_error_msg('Comnpiler is not supported')
            raise TypeError(error_msg)

        return sublcass_matching_compiler_family

    @staticmethod
    @abstractmethod
    def get_supported_compiler_families() -> list[CompilerFamily]:
        raise NotImplementedError()

    @staticmethod
    def get_supported_sanitizers() -> list[CompilerSanitizer]:
        return [CompilerSanitizer.NONE]

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
    @abstractmethod
    def get_c_compiler_name() -> str:
        raise NotImplementedError()

    @staticmethod
    @abstractmethod
    def get_cpp_compiler_name() -> str:
        raise NotImplementedError()

    @classmethod
    @abstractmethod
    def _find_installation_dir_by_compiler_family(cls, compiler_family: CompilerFamily) -> Path:
        raise NotImplementedError()

    @classmethod
    @final
    def _assert_compiler_family(cls, compiler_family: CompilerFamily):
        assert compiler_family in cls.get_supported_compiler_families()
