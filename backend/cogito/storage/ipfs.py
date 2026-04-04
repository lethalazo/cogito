"""IPFS storage backend - encrypted user data on the decentralized web.

User-scoped data (memories, preferences, threads) is encrypted client-side with
AES-256-GCM using a wallet-derived key, then stored on IPFS. IPNS provides mutable
pointers so users can update their data without changing the reference.

Data flow:
1. Client encrypts data with wallet-derived key (crypto module)
2. Encrypted bytes are stored on IPFS → returns CID
3. IPNS name is updated to point to the new CID
4. On retrieval: resolve IPNS → fetch CID from IPFS → return encrypted bytes
5. Client decrypts with wallet-derived key
"""

from typing import Any

from cogito.storage.base import MutableStorageBackend


class IPFSStorage(MutableStorageBackend):
    """IPFS-backed mutable storage for encrypted user data.

    All data stored through this backend should already be encrypted -
    this layer handles content-addressing and pinning, not encryption.

    Requires an IPFS node (local or remote pinning service like Pinata/web3.storage).
    """

    def __init__(self, ipfs_api_url: str = "/ip4/127.0.0.1/tcp/5001") -> None:
        self.ipfs_api_url = ipfs_api_url

    async def store(self, key: str, data: bytes, **metadata: Any) -> str:
        """Pin encrypted data to IPFS and return the CID.

        Args:
            key: Logical key (used for IPNS mapping).
            data: Encrypted bytes to store.
            **metadata: Pin metadata (name, etc.).

        Returns:
            The IPFS CID (content identifier).
        """
        raise NotImplementedError

    async def retrieve(self, key: str) -> bytes:
        """Fetch encrypted data from IPFS by CID or resolved IPNS name.

        Args:
            key: CID or IPNS name.

        Returns:
            Encrypted bytes (caller must decrypt).
        """
        raise NotImplementedError

    async def delete(self, key: str) -> None:
        """Unpin data from IPFS. Data may persist on other nodes."""
        raise NotImplementedError

    async def list_keys(self, prefix: str = "") -> list[str]:
        """List pinned CIDs matching a prefix pattern."""
        raise NotImplementedError

    async def exists(self, key: str) -> bool:
        """Check if a CID is pinned on this node."""
        raise NotImplementedError

    async def update(self, key: str, data: bytes, **metadata: Any) -> str:
        """Store new data and update the IPNS pointer.

        Args:
            key: The IPNS name to update.
            data: New encrypted bytes.
            **metadata: Updated metadata.

        Returns:
            The new CID.
        """
        raise NotImplementedError

    async def resolve(self, mutable_ref: str) -> str:
        """Resolve an IPNS name to its current CID.

        Args:
            mutable_ref: The IPNS name.

        Returns:
            The current CID.
        """
        raise NotImplementedError
