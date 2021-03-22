from pathlib import Path
from typing import Final, Optional

import vswhere

import utils.error.cls_def

_DEFAULT_REQUIRES: Final[list[str]] = [
    'Microsoft.VisualStudio.Component.VC.Tools.x86.x64',
    'Microsoft.VisualStudio.Component.Windows10SDK.19041',
    'Microsoft.VisualStudio.Component.VC.CMake.Project',
    'Microsoft.VisualStudio.Component.TestTools.BuildTools',
    'Microsoft.VisualStudio.Component.VC.ASAN',
    'Microsoft.VisualStudio.Component.VC.Modules.x86.x64',
    'Microsoft.VisualStudio.Workload.VCTools'
]

_ALL_PRODUCTS: Final[str] = '*'
_PROP_INSTALLATION_PATH: Final[str] = 'installationPath'


def find_location(compiler_installation_path: Optional[Path] = None) -> Optional[Path]:
    if compiler_installation_path is None:
        found_compiler_installation_path = vswhere.find_first(latest=True, prerelease=True, products=_ALL_PRODUCTS, prop=_PROP_INSTALLATION_PATH, requires=_DEFAULT_REQUIRES)
    else:
        found_compiler_installation_path = vswhere.find_first(prop=_PROP_INSTALLATION_PATH, path=compiler_installation_path)

    if found_compiler_installation_path is not None:
        try:
            found_compiler_installation_path = Path(found_compiler_installation_path.strip()).resolve(strict=True)

        except FileNotFoundError as raised_error:
            supported_exception = utils.error.cls_def.CompilerNotFoundError()
            supported_exception.with_traceback(raised_error.__traceback__)
            raise supported_exception

    return found_compiler_installation_path
