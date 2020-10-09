import sys
from typing import Any, Dict, Text

if sys.version_info >= (3, 6):
    from os import PathLike

    _Path = PathLike[Text]
else:
    _Path = Text

def validate_system(system: Dict[Text, Any]) -> None: ...
def load_system(source_dir: _Path) -> Dict[Text, Any]: ...
def compat_system(source_dir: _Path) -> Dict[Text, Any]: ...
