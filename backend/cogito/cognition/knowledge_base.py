"""Knowledge base store — structured knowledge as Markdown with YAML frontmatter."""

from pathlib import Path
from typing import Any


class KBStore:
    """Manages the knowledge base: Markdown files with YAML frontmatter + JSONL index.

    The KB stores long-lived, structured knowledge — entities, facts, models, and scripts.
    Each entry is a Markdown file with typed YAML frontmatter. A separate JSONL index
    enables fast semantic search.
    """

    def __init__(self, data_dir: Path) -> None:
        self.data_dir = data_dir

    async def read(self, entity_id: str) -> dict:
        """Load a KB entity by ID.

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
        """Create or update a KB entity.

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

        Args:
            entity_id: The entity to delete.
        """
        raise NotImplementedError

    async def reindex(self) -> int:
        """Rebuild all embeddings and the index file.

        Returns:
            Number of entities re-indexed.
        """
        raise NotImplementedError
