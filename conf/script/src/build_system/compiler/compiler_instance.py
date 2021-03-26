import abc
import dataclasses
import pathlib
import typing

import build_system.compiler.family
import build_system.compiler.host.architecture
import build_system.compiler.host.os_family
import build_system.compiler.version
import utils.cmd_integrity
import utils.error.cls_def


@dataclasses.dataclass(order=True, frozen=True)
class CompilerInstance(metaclass=abc.ABCMeta):
    compiler_family: build_system.compiler.family.CompilerFamily
    os_family: build_system.compiler.host.os_family.OSFamily
    version: build_system.compiler.version.CompilerVersion
    installation_dir: pathlib.Path

    def __init__(self,
                 compiler_family: build_system.compiler.family.CompilerFamily,
                 os_family: build_system.compiler.host.os_family.OSFamily,
                 version: build_system.compiler.version.CompilerVersion,
                 installation_dir: pathlib.Path
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
                                       installation_dir: typing.Optional[pathlib.Path] = None) -> 'CompilerInstance':
        import build_system.cmd.compiler.host.get_info.version.fetch_by_criteria

        if installation_dir is None:
            installation_dir = cls._find_installation_dir_by_compiler_family(compiler_family)

        version = build_system.cmd.compiler.host.get_info.version.fetch_by_criteria.fetch_by_compiler_family(compiler_family)

        return cls(compiler_family=compiler_family, os_family=os_family, version=version, installation_dir=installation_dir)

    @classmethod
    @abc.abstractmethod
    def _find_installation_dir_by_compiler_family(cls, compiler_family: build_system.compiler.family.CompilerFamily) -> pathlib.Path:
        raise NotImplementedError()

    @staticmethod
    @abc.abstractmethod
    def _assert_compiler_family(compiler_family: build_system.compiler.family.CompilerFamily):
        raise NotImplementedError()


class GNUCompilerInstance(CompilerInstance):

    @classmethod
    def _find_installation_dir_by_compiler_family(cls, compiler_family: build_system.compiler.family.CompilerFamily) -> pathlib.Path:
        cls._assert_compiler_family(compiler_family=compiler_family)

        compiler_location, compiler_instance_exists = utils.cmd_integrity.get_cmd_path(compiler_family)

        if not compiler_instance_exists:
            raise utils.error.cls_def.CompilerNotFoundError()

        return compiler_location.parent

    @staticmethod
    def _assert_compiler_family(compiler_family: build_system.compiler.family.CompilerFamily):
        assert compiler_family == build_system.compiler.family.CompilerFamily.GCC \
               or compiler_family == build_system.compiler.family.CompilerFamily.CLANG
