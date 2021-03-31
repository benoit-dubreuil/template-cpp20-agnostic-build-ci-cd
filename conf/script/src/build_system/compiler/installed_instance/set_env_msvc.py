import contextlib


class EnvMSVC(contextlib.AbstractContextManager):
    import build_system.compiler.installed_instance.msvc

    compiler: build_system.compiler.installed_instance.msvc.MSVCCompilerInstance

    def __init__(self, compiler: build_system.compiler.installed_instance.msvc.MSVCCompilerInstance) -> None:
        super().__init__()
        self.compiler = compiler
