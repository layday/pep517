from typing import (
    Any,
    Callable,
    ContextManager,
    Mapping,
    List,
    Sequence,
    Text,
    Union,
)
import sys

if sys.version_info >= (3, 6):
    from os import PathLike

    _Path = PathLike[Text]
else:
    _Path = Text

_SubprocessRunner = Callable[
    [Sequence[str], Text, Mapping[Union[bytes, Text], Union[bytes, Text]]],
    None,
]

class BackendUnavailable(Exception):
    traceback: Text

class BackendInvalid(Exception):
    backend_name: Text
    backend_path: Text
    message: Text

class HookMissing(Exception):
    hook_name: Text

class UnsupportedOperation(Exception):
    traceback: Text

default_subprocess_runner: _SubprocessRunner
quiet_subprocess_runner: _SubprocessRunner

class Pep517HookCaller:
    source_dir: Text
    build_backend: Text
    backend_path: List[Text]
    def __init__(
        self,
        source_dir: _Path,
        build_backend: Text,
        backend_path: Text = ...,
        runner: _SubprocessRunner = ...,
    ) -> None: ...
    def subprocess_runner(
        self, runner: _SubprocessRunner
    ) -> ContextManager[None]: ...
    def get_requires_for_build_wheel(
        self, config_settings: Mapping[Any, Any] = ...
    ) -> List[Text]: ...
    def prepare_metadata_for_build_wheel(
        self,
        metadata_directory: Text,
        config_settings: Mapping[Any, Any] = ...,
        _allow_fallback: bool = ...,
    ) -> Text: ...
    def build_wheel(
        self,
        wheel_directory: Text,
        config_settings: Mapping[Any, Any] = ...,
        metadata_directory: Text = ...,
    ) -> Text: ...
    def get_requires_for_build_sdist(
        self, config_settings: Mapping[Any, Any] = ...
    ) -> List[Text]: ...
    def build_sdist(
        self, sdist_directory: Text, config_settings: Mapping[Any, Any] = ...
    ) -> Text: ...
