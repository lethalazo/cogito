"""Memory store - persistent, scored, multi-tier memory with decentralized storage.

User-scoped memories are encrypted client-side and stored on IPFS (or local storage
for self-hosted nodes). The platform never sees plaintext user memories.

Shared memories (agent-tier, global-tier) are stored on Arweave as part of the
agent's world model - public and permanent.

During active sessions:
1. Fetch encrypted memories from user storage → decrypt client-side
2. Agent processes memories in-memory for context injection
3. New learnings are encrypted → stored back to user storage
"""

from typing import Any

from cogito.storage.base import StorageBackend


class MemoryStore:
    """Manages memory storage, retrieval, and maintenance.

    Operates across two storage backends:
    - user_storage: Encrypted user memories (IPFS or local)
    - shared_storage: Public agent/global memories (Arweave or local)
    """

    def __init__(
        self, user_storage: StorageBackend, shared_storage: StorageBackend
    ) -> None:
        self.user_storage = user_storage
        self.shared_storage = shared_storage

    async def store(
        self,
        content: str,
        tier: str,
        memory_type: str,
        tags: list[str] | None = None,
        wallet_address: str | None = None,
        agent_id: str | None = None,
        source_thread: str | None = None,
        metadata: dict[str, Any] | None = None,
        encryption_key: bytes | None = None,
    ) -> dict:
        """Create a new memory entry with generated embedding.

        User-tier memories are encrypted with the provided key before storage.
        Agent/global-tier memories are stored unencrypted in shared storage.

        Args:
            content: The memory content text.
            tier: "global", "user", or "agent".
            memory_type: "observation", "inference", "preference", "fact", or "episode".
            tags: Optional categorization tags.
            wallet_address: Wallet address (required for user-tier memories).
            agent_id: Agent ID (required for agent-tier memories).
            source_thread: Thread ID where this memory originated.
            metadata: Additional metadata.
            encryption_key: AES-256 key for encrypting user-tier memories.

        Returns:
            The created memory entry.
        """
        raise NotImplementedError

    async def recall(
        self,
        query: str,
        tier: str | None = None,
        wallet_address: str | None = None,
        agent_id: str | None = None,
        limit: int = 10,
        decryption_key: bytes | None = None,
    ) -> list[dict]:
        """Recall memories by semantic similarity with scoring.

        User-tier memories are decrypted in-memory using the provided key.

        Args:
            query: The search query.
            tier: Optional tier filter.
            wallet_address: Wallet address for user-scoped recall.
            agent_id: Optional agent scope.
            limit: Maximum results.
            decryption_key: AES-256 key for decrypting user-tier memories.

        Returns:
            Memories ranked by composite score.
        """
        raise NotImplementedError

    async def query(
        self,
        tier: str | None = None,
        memory_type: str | None = None,
        tags: list[str] | None = None,
        wallet_address: str | None = None,
        agent_id: str | None = None,
        decryption_key: bytes | None = None,
    ) -> list[dict]:
        """Filter memories by structured criteria.

        Args:
            tier: Filter by tier.
            memory_type: Filter by type.
            tags: Filter by tags (any match).
            wallet_address: Filter by wallet address.
            agent_id: Filter by agent.
            decryption_key: AES-256 key for decrypting user-tier results.

        Returns:
            Matching memories.
        """
        raise NotImplementedError

    async def update(self, memory_id: str, encryption_key: bytes | None = None, **fields: Any) -> dict:
        """Update specific fields of a memory.

        If the memory is user-scoped, the updated entry is re-encrypted.

        Args:
            memory_id: The memory to update.
            encryption_key: AES-256 key for re-encrypting user-tier memories.
            **fields: Fields to update.

        Returns:
            The updated memory.
        """
        raise NotImplementedError

    async def prune(
        self,
        threshold: float,
        wallet_address: str | None = None,
        decryption_key: bytes | None = None,
    ) -> list[str]:
        """Remove memories with composite scores below the threshold.

        User-tier pruning requires decryption key to evaluate scores.

        Args:
            threshold: Minimum score to keep.
            wallet_address: Scope pruning to a specific wallet's memories.
            decryption_key: AES-256 key for evaluating encrypted memory scores.

        Returns:
            IDs of pruned memories.
        """
        raise NotImplementedError

    async def consolidate(
        self,
        memory_ids: list[str],
        encryption_key: bytes | None = None,
    ) -> dict:
        """Merge similar memories into a single stronger entry.

        If consolidating user-tier memories, the merged result is re-encrypted.

        Args:
            memory_ids: IDs of memories to consolidate.
            encryption_key: AES-256 key for user-tier memory operations.

        Returns:
            The consolidated memory.
        """
        raise NotImplementedError

    async def supersede(self, old_id: str, new_id: str) -> None:
        """Mark a memory as replaced by a newer version.

        Args:
            old_id: The memory being superseded.
            new_id: The replacement memory.
        """
        raise NotImplementedError
