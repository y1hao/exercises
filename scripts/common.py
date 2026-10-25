"""Shared YAML and repository-path handling; no network or writes on import."""

from pathlib import Path, PurePosixPath
import re

import yaml

ROOT = Path(__file__).resolve().parents[1]
STATUSES = {"candidate", "sourced", "ready", "blocked", "rejected"}
DOMAINS = {"engineering", "product", "investing"}
KINDS = {"historical", "micro_design"}


class UniqueKeyLoader(yaml.SafeLoader):
    """Reject duplicate keys rather than silently keeping the last value."""


def _mapping(loader, node):
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node)
        try:
            duplicate = key in result
        except TypeError as exc:
            raise ValueError("YAML mapping keys must be scalar") from exc
        if duplicate:
            raise ValueError(f"Duplicate YAML key: {key!r}")
        result[key] = loader.construct_object(value_node)
    return result


UniqueKeyLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _mapping
)


def read_yaml(path):
    return yaml.load(Path(path).read_text(encoding="utf-8"), Loader=UniqueKeyLoader)


def write_yaml(path, data):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        yaml.safe_dump(data, allow_unicode=True, sort_keys=False, width=100),
        encoding="utf-8",
    )


def local_path(root, value):
    """Accept only canonical relative POSIX paths resolving inside root."""
    if not isinstance(value, str) or not value or "\\" in value:
        raise ValueError("expected a nonempty repository-relative POSIX path")
    rel = PurePosixPath(value)
    if (
        rel.is_absolute()
        or any(part in {"", ".", ".."} for part in value.split("/"))
        or re.search(r"[:?#%\x00-\x1f]", value)
    ):
        raise ValueError(f"unsafe repository path: {value!r}")
    target = (Path(root) / value).resolve()
    if not target.is_relative_to(Path(root).resolve()):
        raise ValueError(f"path escapes repository: {value!r}")
    if not target.is_file():
        raise ValueError(f"file does not exist: {value}")
    return target
