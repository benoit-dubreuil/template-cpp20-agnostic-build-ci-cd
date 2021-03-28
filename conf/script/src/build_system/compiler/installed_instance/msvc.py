from pathlib import Path

import build_system.compiler.family
import build_system.compiler.installed_instance.compiler_instance


class MSVCCompilerInstance(build_system.compiler.installed_instance.CompilerInstance):
    vcvars_arch_batch_file: Path

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        object.__setattr__(self, 'vcvars_arch_batch_file', self.__find_vcvars_batch_file())

    @classmethod
    def _find_installation_dir_by_compiler_family(cls, compiler_family: build_system.compiler.family.CompilerFamily) -> Path:
        import build_system.cmd.compiler.host.get_info.location.msvc

        cls._assert_compiler_family(compiler_family=compiler_family)

        compiler_installation_dir = build_system.cmd.compiler.host.get_info.location.msvc.find_location()
        return compiler_installation_dir

    @staticmethod
    def get_supported_compiler_families() -> list[build_system.compiler.family.CompilerFamily]:
        return [build_system.compiler.family.CompilerFamily.MSVC]

    @staticmethod
    def get_vcvars_dir_relative_to_installation_dir() -> Path:
        return Path('VC/Auxiliary/Build')

    @staticmethod
    def get_vcvars_prefix() -> str:
        return 'vcvars'

    @staticmethod
    def get_vcvars_extension() -> str:
        return '.bat'

    def __get_vcvars_dir(self) -> Path:
        return self.installation_dir / self.get_vcvars_dir_relative_to_installation_dir()

    def __compute_vcvars_arch_batch_filename(self) -> str:
        return self.get_vcvars_prefix() + self.arch.value + self.get_vcvars_extension()

    def __find_vcvars_batch_file(self) -> Path:
        vcvars_dir: Path = self.__get_vcvars_dir()
        vcvars_filename: str = self.__compute_vcvars_arch_batch_filename()
        vcvars_arch_batch_file = vcvars_dir / vcvars_filename

        # TODO : Add custom exception
        # TODO : try-catch
        vcvars_arch_batch_file.resolve(strict=True)

        return vcvars_arch_batch_file
