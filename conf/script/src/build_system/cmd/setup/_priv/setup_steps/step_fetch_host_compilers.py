__all__ = ['fetch_host_compilers']

from build_system.compiler import *


def fetch_host_compilers() -> list[CompilerInstance]:
    host_compilers = fetch_supported_installed_compiler_instances()
    return host_compilers
