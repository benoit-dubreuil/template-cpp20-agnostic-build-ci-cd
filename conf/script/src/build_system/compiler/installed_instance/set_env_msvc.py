import contextlib


class EnvMSVC(contextlib.AbstractContextManager):
    import build_system.compiler.installed_instance.msvc

    compiler: build_system.compiler.installed_instance.msvc.MSVCCompilerInstance
    ...
