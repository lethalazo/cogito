"""Knowledge base store - structured knowledge on decentralized storage.

The knowledge base is part of the agent's shared cognition - the world model.
Stored on Arweave (permanent, public, immutable) or local storage for dev/self-hosted.

KB entities are public and unencrypted - they contain world knowledge (entities, facts,
models, scripts), never user-specific information. Self-hosted nodes read KB data from
Arweave (read-only) to stay in sync with the shared world model.
"""

from typing import Any

from cogito.storage.base import StorageBackend


class KBStore:
    """Manages the knowledge base: Markdown files with YAML frontmatter.

    Uses a StorageBackend for persistence - Arweave for production (permanent, public),
    local filesystem for development and self-hosted nodes.
    """

    def __init__(self, storage: StorageBackend) -> None:
        self.storage = storage

    async def read(self, entity_id: str) -> dict:
        """Load a KB entity by ID from storage.

        Args:
            entity_id: The entity ID (e.g., "kb_xxx").

        Returns:
            The entity with parsed frontmatter and content.
        """
        raise NotImplementedError

    async def write(
        self,
        content: str,
        entity_type: str,
        title: str,
        tags: list[str] | None = None,
        numerical_facts: dict[str, Any] | None = None,
        metadata: dict[str, Any] | None = None,
    ) -> dict:
        """Create or update a KB entity in storage.

        On Arweave, updates create new transactions (append-only).
        The latest transaction for a given entity ID is the current version.

        Args:
            content: The Markdown content body.
            entity_type: "entity", "fact", "model", or "script".
            title: The entity title.
            tags: Categorization tags.
            numerical_facts: Structured numerical data.
            metadata: Additional metadata.

        Returns:
            The created/updated entity with generated embedding.
        """
        raise NotImplementedError

    async def search(
        self,
        query: str,
        entity_type: str | None = None,
        tags: list[str] | None = None,
        limit: int = 10,
    ) -> list[dict]:
        """Semantic search over the KB index.

        Args:
            query: The search query.
            entity_type: Optional type filter.
            tags: Optional tag filter.
            limit: Maximum results.

        Returns:
            Matching index entries ranked by similarity.
        """
        raise NotImplementedError

    async def list(
        self,
        entity_type: str | None = None,
        tags: list[str] | None = None,
    ) -> list[dict]:
        """List entities matching filters.

        Args:
            entity_type: Optional type filter.
            tags: Optional tag filter.

        Returns:
            Matching index entries.
        """
        raise NotImplementedError

    async def delete(self, entity_id: str) -> None:
        """Remove an entity and its index entry.

        On Arweave, this marks the entity as deleted (append-only) rather than
        physically removing it. On local storage, the file is deleted.

        Args:
            entity_id: The entity to delete.
        """
        raise NotImplementedError

    async def reindex(self) -> int:
        """Rebuild all embeddings and the index.

        Uses public embedding model (Voyage AI) for shared cognition.

        Returns:
            Number of entities re-indexed.
        """
        raise NotImplementedError
