import abc
from dataclasses import dataclass
from pathlib import Path
from typing import Optional, Type

import build_system.compiler.family
import build_system.compiler.host.architecture
import build_system.compiler.host.os_family
import build_system.compiler.version
import utils.cmd_integrity
import utils.error.cls_def
import utils.error.format


@dataclass(order=True, frozen=True)
class CompilerInstance(metaclass=abc.ABCMeta):
    compiler_family: build_system.compiler.family.CompilerFamily
    os_family: build_system.compiler.host.os_family.OSFamily
    version: build_system.compiler.version.CompilerVersion
    installation_dir: Path

    def __init__(self,
                 compiler_family: build_system.compiler.family.CompilerFamily,
                 os_family: build_system.compiler.host.os_family.OSFamily,
                 version: build_system.compiler.version.CompilerVersion,
                 installation_dir: Path
                 ):
        self._assert_compiler_family(compiler_family=compiler_family)

        object.__setattr__(self, 'compiler_family', compiler_family)
        object.__setattr__(self, 'os_family', os_family)
        object.__setattr__(self, 'version', version)
        object.__setattr__(self, 'installation_dir', installation_dir)

    @classmethod
    def create_from_installed_compiler(cls,
                                       compiler_family: build_system.compiler.family.CompilerFamily,
                                       os_family: build_system.compiler.host.os_family.OSFamily,
                                       installation_dir: Optional[Path] = None) -> 'CompilerInstance':
        import build_system.cmd.compiler.host.get_info.version.fetch_by_criteria

        sub_cls_matching_compiler_family: Type[CompilerInstance] = cls.__checked_search_first_sub_cls_matching_compiler_family(compiler_family=compiler_family)

        if installation_dir is None:
            installation_dir = sub_cls_matching_compiler_family._find_installation_dir_by_compiler_family(compiler_family=compiler_family)
        else:
            try:
                installation_dir.resolve(strict=True)
            except Exception as raised_error:
                supported_exception = utils.error.cls_def.CompilerNotFoundError()
                supported_exception.with_traceback(raised_error.__traceback__)

                raise supported_exception

        version = build_system.cmd.compiler.host.get_info.version.fetch_by_criteria.fetch_by_compiler_family(compiler_family)

        return sub_cls_matching_compiler_family(compiler_family=compiler_family, os_family=os_family, version=version, installation_dir=installation_dir)

    @classmethod
    def __search_first_sub_cls_matching_compiler_family(cls, compiler_family: build_system.compiler.family.CompilerFamily) -> Optional[Type['CompilerInstance']]:
        subclasses: list[Type[CompilerInstance]] = cls.__subclasses__()
        sublcass_matching_compiler_family: Optional[Type[CompilerInstance]] = None

        while subclasses and subclasses:
            concrete_subclass = subclasses.pop(-1)

            if compiler_family in concrete_subclass.get_supported_compiler_families():
                sublcass_matching_compiler_family = concrete_subclass

        return sublcass_matching_compiler_family

    @classmethod
    def __checked_search_first_sub_cls_matching_compiler_family(cls, compiler_family: build_system.compiler.family.CompilerFamily) -> Type['CompilerInstance']:
        sublcass_matching_compiler_family: Optional[Type[CompilerInstance]] = cls.__search_first_sub_cls_matching_compiler_family(compiler_family=compiler_family)

        if sublcass_matching_compiler_family is None:
            error_msg: str = utils.error.format.format_error_msg('Comnpiler is not supported')
            raise TypeError(error_msg)

        return sublcass_matching_compiler_family

    @staticmethod
    @abc.abstractmethod
    def get_supported_compiler_families() -> list[build_system.compiler.family.CompilerFamily]:
        raise NotImplementedError()

    @classmethod
    @abc.abstractmethod
    def _find_installation_dir_by_compiler_family(cls, compiler_family: build_system.compiler.family.CompilerFamily) -> Path:
        raise NotImplementedError()

    @classmethod
    def _assert_compiler_family(cls, compiler_family: build_system.compiler.family.CompilerFamily):
        assert compiler_family in cls.get_supported_compiler_families()


@dataclass(order=True, frozen=True)
class GNUCompilerInstance(CompilerInstance):
    executable_file: Path

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        object.__setattr__(self, 'executable_file', self.__get_executable_file_from_installation_dir())

    def __get_executable_file_from_installation_dir(self) -> Path:
        executable_file, exists = utils.cmd_integrity.get_cmd_path(cmd=self.compiler_family.value, dir_path=self.installation_dir)

        if not exists:
            raise utils.error.cls_def.CompilerNotFoundError()

        try:
            executable_file.resolve(strict=True)

        except Exception as raised_error:
            supported_exception = utils.error.cls_def.CompilerNotFoundError()
            supported_exception.with_traceback(raised_error.__traceback__)

            raise supported_exception

        return executable_file

    @classmethod
    def _find_installation_dir_by_compiler_family(cls, compiler_family: build_system.compiler.family.CompilerFamily) -> Path:
        cls._assert_compiler_family(compiler_family=compiler_family)

        compiler_location, compiler_instance_exists = utils.cmd_integrity.get_cmd_path(cmd=compiler_family.value)

        if not compiler_instance_exists:
            raise utils.error.cls_def.CompilerNotFoundError()

        compiler_installation_dir = compiler_location.parent

        return compiler_installation_dir

    @staticmethod
    def get_supported_compiler_families() -> list[build_system.compiler.family.CompilerFamily]:
        return [build_system.compiler.family.CompilerFamily.GCC,
                build_system.compiler.family.CompilerFamily.CLANG]


class MSVCCompilerInstance(CompilerInstance):

    @classmethod
    def _find_installation_dir_by_compiler_family(cls, compiler_family: build_system.compiler.family.CompilerFamily) -> Path:
        import build_system.cmd.compiler.host.get_info.location.msvc

        cls._assert_compiler_family(compiler_family=compiler_family)

        compiler_installation_dir = build_system.cmd.compiler.host.get_info.location.msvc.find_location()
        return compiler_installation_dir

    @staticmethod
    def get_supported_compiler_families() -> list[build_system.compiler.family.CompilerFamily]:
        return [build_system.compiler.family.CompilerFamily.MSVC]
