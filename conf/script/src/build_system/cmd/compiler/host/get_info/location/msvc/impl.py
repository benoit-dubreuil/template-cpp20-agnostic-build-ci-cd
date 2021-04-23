from pathlib import Path
from typing import Final, Optional

import vswhere

from build_system.compiler import *
from ext.error import *
from ext.error.utils import *

from ext.meta_prog.encapsulation import *

DEFAULT_REQUIRES: Final[list[str]] = [
    'Microsoft.VisualStudio.Component.VC.Tools.x86.x64',
    'Microsoft.VisualStudio.Component.Windows10SDK.19041',
    'Microsoft.VisualStudio.Component.VC.CMake.Project',
    'Microsoft.VisualStudio.Component.TestTools.BuildTools',
    'Microsoft.VisualStudio.Component.VC.ASAN',
    'Microsoft.VisualStudio.Component.VC.Modules.x86.x64',
    'Microsoft.VisualStudio.Workload.VCTools'
]

ALL_PRODUCTS: Final[str] = '*'
PROP_INSTALLATION_PATH: Final[str] = 'installationPath'


@export
def find_msvc_location(compiler_installation_path: Optional[Path] = None) -> Optional[Path]:
    if compiler_installation_path is None:
        found_compiler_installation_path = vswhere.find_first(latest=True, prerelease=True, products=ALL_PRODUCTS, prop=PROP_INSTALLATION_PATH, requires=DEFAULT_REQUIRES)
    else:
        found_compiler_installation_path = vswhere.find_first(prop=PROP_INSTALLATION_PATH, path=compiler_installation_path)

    if found_compiler_installation_path is not None:
        found_compiler_installation_path = Path(found_compiler_installation_path.strip())

        try_manage_strict_path_resolving(path_to_resolve=found_compiler_installation_path,
                                         external_errors_to_manage={(Exception,): CompilerNotFoundError})

        found_compiler_installation_path = found_compiler_installation_path.absolute()

    return found_compiler_installation_path
