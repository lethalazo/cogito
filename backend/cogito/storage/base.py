"""Abstract base classes for decentralized storage backends.

Two backend categories:
- MutableStorageBackend (IPFS, local) — for user data that can be updated and deleted
- ImmutableStorageBackend (Arweave) — for shared cognition that is permanent and append-only
"""

from abc import ABC, abstractmethod
from typing import Any


class StorageBackend(ABC):
    """Base interface for all storage backends."""

    @abstractmethod
    async def store(self, key: str, data: bytes, **metadata: Any) -> str:
        """Store data and return a content-addressable identifier.

        Args:
            key: Logical key for the data (e.g., "memories/mem_abc123").
            data: Raw bytes to store (already encrypted for user-scoped data).
            **metadata: Backend-specific metadata (tags, content-type, etc.).

        Returns:
            A content identifier (CID for IPFS, transaction ID for Arweave, path for local).
        """
        ...

    @abstractmethod
    async def retrieve(self, key: str) -> bytes:
        """Retrieve data by key or content identifier.

        Args:
            key: The key or content identifier.

        Returns:
            The raw bytes (still encrypted for user-scoped data — caller must decrypt).
        """
        ...

    @abstractmethod
    async def delete(self, key: str) -> None:
        """Delete data by key. No-op on immutable backends.

        Args:
            key: The key or content identifier.
        """
        ...

    @abstractmethod
    async def list_keys(self, prefix: str = "") -> list[str]:
        """List all keys matching a prefix.

        Args:
            prefix: Key prefix to filter by.

        Returns:
            List of matching keys.
        """
        ...

    @abstractmethod
    async def exists(self, key: str) -> bool:
        """Check whether a key exists in storage.

        Args:
            key: The key or content identifier.

        Returns:
            True if the key exists.
        """
        ...


class MutableStorageBackend(StorageBackend):
    """Storage backend that supports updates and mutable references.

    Used for IPFS (via IPNS for mutable pointers) and local filesystem.
    User-scoped data lives here — encrypted, pinned, and updatable.
    """

    @abstractmethod
    async def update(self, key: str, data: bytes, **metadata: Any) -> str:
        """Update existing data at a key.

        Args:
            key: The key to update.
            data: New raw bytes.
            **metadata: Updated metadata.

        Returns:
            The new content identifier.
        """
        ...

    @abstractmethod
    async def resolve(self, mutable_ref: str) -> str:
        """Resolve a mutable reference (e.g., IPNS name) to a content identifier.

        Args:
            mutable_ref: The mutable reference to resolve.

        Returns:
            The current content identifier.
        """
        ...


class ImmutableStorageBackend(StorageBackend):
    """Storage backend for permanent, append-only data.

    Used for Arweave. Shared cognition (KB, graph, world model) lives here —
    public, permanent, and queryable by tags.
    """

    @abstractmethod
    async def query_by_tags(self, tags: dict[str, str]) -> list[str]:
        """Query stored data by Arweave-style tags.

        Args:
            tags: Tag key-value pairs to match (e.g., {"Content-Type": "application/json"}).

        Returns:
            List of matching transaction IDs.
        """
        ...

    async def delete(self, key: str) -> None:
        """No-op — immutable storage cannot delete data."""
        pass
