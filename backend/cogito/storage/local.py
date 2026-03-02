"""Local filesystem storage backend — for development and self-hosted nodes.

Implements MutableStorageBackend using the local filesystem. Data is stored as files
under a configurable root directory, preserving the same key structure used by IPFS.

In production self-hosted deployments, this backend stores encrypted user data locally
instead of pinning to IPFS — the user's node is their own infrastructure.
"""

from pathlib import Path
from typing import Any

from cogito.storage.base import MutableStorageBackend


class LocalStorage(MutableStorageBackend):
    """Filesystem-backed mutable storage for dev and self-hosted deployments.

    Keys map to file paths under the root directory. Data is stored as raw bytes —
    encryption is handled by the caller (crypto module) before reaching this layer.
    """

    def __init__(self, root_dir: Path) -> None:
        self.root_dir = root_dir

    async def store(self, key: str, data: bytes, **metadata: Any) -> str:
        """Store data as a file under root_dir/key.

        Returns:
            The key (acts as the content identifier for local storage).
        """
        raise NotImplementedError

    async def retrieve(self, key: str) -> bytes:
        """Read file contents from root_dir/key."""
        raise NotImplementedError

    async def delete(self, key: str) -> None:
        """Delete the file at root_dir/key."""
        raise NotImplementedError

    async def list_keys(self, prefix: str = "") -> list[str]:
        """List all files under root_dir matching the prefix."""
        raise NotImplementedError

    async def exists(self, key: str) -> bool:
        """Check if a file exists at root_dir/key."""
        raise NotImplementedError

    async def update(self, key: str, data: bytes, **metadata: Any) -> str:
        """Overwrite the file at root_dir/key with new data."""
        raise NotImplementedError

    async def resolve(self, mutable_ref: str) -> str:
        """Identity resolution — local keys are already resolved."""
        raise NotImplementedError
