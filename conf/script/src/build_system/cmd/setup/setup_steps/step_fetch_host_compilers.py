import build_system.compiler.installed_instance
import build_system.compiler.supported_installed_instances


def fetch_host_compilers() -> list[build_system.compiler.installed_instance.CompilerInstance]:
    host_compilers = build_system.compiler.supported_installed_instances.fetch_all()
    return host_compilers
