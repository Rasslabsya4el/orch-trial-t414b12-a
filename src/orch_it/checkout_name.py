"""Whether the checkout folder carries the repo's name (planted by #414 live row 12; no literal of either name)."""

import subprocess
from pathlib import Path


def repo_name(root: Path) -> str:
    """The last segment of the origin URL of the checkout at `root`, without a `.git` tail."""
    url = subprocess.run(["git", "config", "remote.origin.url"], cwd=root, capture_output=True, text=True,
                         check=True).stdout.strip()
    return url.rstrip("/").rsplit("/", 1)[-1].removesuffix(".git")


def folder_is_repo_name(root: Path) -> bool:
    return root.name == repo_name(root)
