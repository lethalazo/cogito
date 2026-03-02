"""Decentralized storage abstraction — IPFS for user data, Arweave for shared cognition."""

from cogito.storage.base import (
    ImmutableStorageBackend,
    MutableStorageBackend,
    StorageBackend,
)

__all__ = [
    "StorageBackend",
    "MutableStorageBackend",
    "ImmutableStorageBackend",
]
