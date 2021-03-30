import dataclasses
import typing

import build_system.build_target.build_type
import build_system.compiler.host.architecture
import build_system.compiler.installed_instance


@dataclasses.dataclass(order=True, frozen=True)
class TargetBuildName:
    compiler_instance: build_system.compiler.installed_instance.CompilerInstance
    target_build_type: build_system.build_target.build_type.TargetBuildType

    def __str__(self) -> str:
        sep: typing.Final[str] = self.get_name_separator()
        os_family_name = self.compiler_instance.os_family.value
        arch_bit_name = self.compiler_instance.arch.arch_to_bit_name()
        compiler_name = self.compiler_instance.compiler_family.value
        compiler_version_name = str(self.compiler_instance.version)
        target_build_type_name = self.target_build_type.value

        return os_family_name + sep + arch_bit_name + sep + compiler_name + sep + compiler_version_name + sep + target_build_type_name

    @staticmethod
    def get_name_separator() -> str:
        return '-'
