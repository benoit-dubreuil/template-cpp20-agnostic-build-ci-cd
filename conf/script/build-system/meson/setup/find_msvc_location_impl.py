from pathlib import Path
from typing import Final, Optional

import vswhere

DEFAULT_REQUIRES: Final[list[str]] = [
    'Microsoft.VisualStudio.Component.VC.Tools.x86.x64',
    'Microsoft.VisualStudio.Component.Windows10SDK.19041',
    'Microsoft.VisualStudio.Component.VC.CMake.Project',
    'Microsoft.VisualStudio.Component.TestTools.BuildTools',
    'Microsoft.VisualStudio.Component.VC.ASAN',
    'Microsoft.VisualStudio.Component.VC.Modules.x86.x64',
    'Microsoft.VisualStudio.Workload.VCTools'
]

_ALL_PRODUCTS: Final[str] = '*'
_PROP_VERSION: Final[str] = 'installationVersion'
_PROP_INSTALLATION_PATH: Final[str] = 'installationPath'


def find_msvc_installation_path() -> Optional[Path]:
    compiler_installation_path: Optional[Path] = None
    found_compiler_version: str = vswhere.find_first(latest=True, prerelease=True, products=_ALL_PRODUCTS, prop=_PROP_INSTALLATION_PATH, requires=DEFAULT_REQUIRES)

    if found_compiler_version is not None:
        compiler_installation_path = Path(found_compiler_version.strip())

    return compiler_installation_path
