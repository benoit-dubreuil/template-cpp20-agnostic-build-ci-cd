__all__ = ['MesonConanPkgRecipe']

from build_system.compiler import *
from build_system.build_target import *
from host import *
from conans import ConanFile, tools, Meson
import os


class MesonConanPkgRecipe(ConanFile):
    _cppstd = 20
    _compilers_reqs: dict[CompilerFamily, CompilerReqs] = CompilerReqs.create_all_from_config_file()

    generators = 'pkg_config'

    requires = ('opengl/system',
                'glfw/3.3.4',
                'glbinding/3.1.0')

    settings = {'os': {{OSFamily.WINDOWS: {'subsystem': None}},
                       OSFamily.LINUX},

                'compiler': {
                    {CompilerFamily.MSVC: {'cppstd': _cppstd,
                                           'version': '19.29'}},

                    {CompilerFamily.CLANG: {'cppstd': _cppstd,
                                            'version': _compilers_reqs[CompilerFamily.CLANG].min_compiler_version.major,
                                            'libcxx': 'libc++'}},

                    {CompilerFamily.GCC: {'cppstd': _cppstd,
                                          'version': _compilers_reqs[CompilerFamily.GCC].min_compiler_version.major,
                                          'libcxx': 'libstdc++11'}}
                },

                'build_type': [TargetBuildType.DEBUG,
                               TargetBuildType.DEBUG_OPTIMIZED.capitalized_alternative_name,
                               TargetBuildType.RELEASE],

                'arch': ['x86_64']}

    def build(self):
        meson = Meson(self)
        meson.configure(build_folder="build")
        meson.build()
