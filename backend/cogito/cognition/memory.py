"""Memory store — persistent, scored, multi-tier memory backed by JSONL."""

from pathlib import Path
from typing import Any


class MemoryStore:
    """Manages memory storage, retrieval, and maintenance.

    Memories are stored as JSONL files, scoped by tier (global, user, agent).
    Each memory has an embedding for semantic search and scores for ranking.
    """

    def __init__(self, data_dir: Path) -> None:
        self.data_dir = data_dir

    async def store(
        self,
        content: str,
        tier: str,
        memory_type: str,
        tags: list[str] | None = None,
        user_id: str | None = None,
        agent_id: str | None = None,
        source_thread: str | None = None,
        metadata: dict[str, Any] | None = None,
    ) -> dict:
        """Create a new memory entry with generated embedding.

        Args:
            content: The memory content text.
            tier: "global", "user", or "agent".
            memory_type: "observation", "inference", "preference", "fact", or "episode".
            tags: Optional categorization tags.
            user_id: User ID (required for user-tier memories).
            agent_id: Agent ID (required for agent-tier memories).
            source_thread: Thread ID where this memory originated.
            metadata: Additional metadata.

        Returns:
            The created memory entry.
        """
        raise NotImplementedError

    async def recall(
        self,
        query: str,
        tier: str | None = None,
        user_id: str | None = None,
        agent_id: str | None = None,
        limit: int = 10,
    ) -> list[dict]:
        """Recall memories by semantic similarity with scoring.

        Args:
            query: The search query.
            tier: Optional tier filter.
            user_id: Optional user scope.
            agent_id: Optional agent scope.
            limit: Maximum results.

        Returns:
            Memories ranked by composite score.
        """
        raise NotImplementedError

    async def query(
        self,
        tier: str | None = None,
        memory_type: str | None = None,
        tags: list[str] | None = None,
        user_id: str | None = None,
        agent_id: str | None = None,
    ) -> list[dict]:
        """Filter memories by structured criteria.

        Args:
            tier: Filter by tier.
            memory_type: Filter by type.
            tags: Filter by tags (any match).
            user_id: Filter by user.
            agent_id: Filter by agent.

        Returns:
            Matching memories.
        """
        raise NotImplementedError

    async def update(self, memory_id: str, **fields: Any) -> dict:
        """Update specific fields of a memory.

        Args:
            memory_id: The memory to update.
            **fields: Fields to update.

        Returns:
            The updated memory.
        """
        raise NotImplementedError

    async def prune(self, threshold: float) -> list[str]:
        """Remove memories with composite scores below the threshold.

        Args:
            threshold: Minimum score to keep.

        Returns:
            IDs of pruned memories.
        """
        raise NotImplementedError

    async def consolidate(self, memory_ids: list[str]) -> dict:
        """Merge similar memories into a single stronger entry.

        Args:
            memory_ids: IDs of memories to consolidate.

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
