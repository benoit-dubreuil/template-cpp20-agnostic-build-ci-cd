import dataclasses
import typing

import build_system.build_target.build_type
import build_system.compiler.compiler_instance
import build_system.compiler.host.architecture


@dataclasses.dataclass(order=True, frozen=True)
class TargetBuildName:
    compiler_instance: build_system.compiler.compiler_instance.CompilerInstance
    arch: build_system.compiler.host.architecture.Architecture
    target_build_type: build_system.build_target.build_type.TargetBuildType

    def __str__(self) -> str:
        sep: typing.Final[str] = self.get_name_separator()
        os_family_name = self.compiler_instance.get_current_os_family().value
        arch_bit_name = self.arch.arch_to_bit_name()
        compiler_name = self.compiler_instance.compiler_family.value
        compiler_version_name = str(self.compiler_instance.version)
        target_build_type_name = self.target_build_type.value

        return os_family_name + sep + arch_bit_name + sep + compiler_name + sep + compiler_version_name + sep + target_build_type_name

    @staticmethod
    def get_name_separator() -> str:
        return '-'
