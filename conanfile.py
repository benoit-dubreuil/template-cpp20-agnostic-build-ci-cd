#!/usr/bin/env python3

__all__ = ['MesonConanPkgRecipe']

from build_system.compiler import *
from build_system.build_target import *
from host import *
from conans import ConanFile, tools, Meson
import os


class MesonConanPkgRecipe(ConanFile):
    generators = 'pkg_config'

    requires = ('opengl/system',
                'glfw/3.3.4',
                'glbinding/3.1.0')

    settings = {'os': {{OSFamily.WINDOWS.value: {'subsystem': None}},
                       OSFamily.LINUX.value},
                'compiler': None,
                'build_type': [TargetBuildType.DEBUG],
                'arch': ['x86_64']}

    def build(self):
        meson = Meson(self)
        meson.configure(build_folder="build")
        meson.build()
