"""Knowledge graph store — nodes and edges backed by JSONL."""

from pathlib import Path
from typing import Any


class GraphStore:
    """Manages the knowledge graph: typed nodes connected by weighted edges.

    Nodes represent concepts, entities, assets, people, etc.
    Edges represent relationships: impacts, causes, owns, related_to, etc.
    Both are stored as JSONL files with embeddings for semantic search.
    """

    def __init__(self, data_dir: Path) -> None:
        self.data_dir = data_dir

    async def add_node(
        self,
        node_type: str,
        label: str,
        tags: list[str] | None = None,
        metadata: dict[str, Any] | None = None,
    ) -> dict:
        """Create a graph node with generated embedding.

        Args:
            node_type: "concept", "entity", "asset", "person", "stock", "file", or "event".
            label: Human-readable label.
            tags: Categorization tags.
            metadata: Additional metadata.

        Returns:
            The created node.
        """
        raise NotImplementedError

    async def add_edge(
        self,
        source: str,
        target: str,
        edge_type: str,
        weight: float = 1.0,
        label: str = "",
        tags: list[str] | None = None,
        metadata: dict[str, Any] | None = None,
    ) -> dict:
        """Create an edge between two nodes.

        Args:
            source: Source node ID.
            target: Target node ID.
            edge_type: "conceptual", "impacts", "owns", "related_to", or "causes".
            weight: Edge weight (0.0 to 1.0).
            label: Human-readable description.
            tags: Categorization tags.
            metadata: Additional metadata.

        Returns:
            The created edge.
        """
        raise NotImplementedError

    async def get_node(self, node_id: str) -> dict:
        """Retrieve a node by ID.

        Args:
            node_id: The node ID.

        Returns:
            The node data.
        """
        raise NotImplementedError

    async def get_neighbors(
        self,
        node_id: str,
        edge_type: str | None = None,
        depth: int = 1,
    ) -> list[dict]:
        """Traverse graph from a node to find connected nodes.

        Args:
            node_id: The starting node.
            edge_type: Optional filter for edge type.
            depth: How many hops to traverse.

        Returns:
            Connected nodes with their edges.
        """
        raise NotImplementedError

    async def query(
        self,
        query: str,
        node_type: str | None = None,
        limit: int = 10,
    ) -> list[dict]:
        """Semantic search over graph nodes.

        Args:
            query: The search query.
            node_type: Optional node type filter.
            limit: Maximum results.

        Returns:
            Matching nodes ranked by similarity.
        """
        raise NotImplementedError

    async def shortest_path(self, source: str, target: str) -> list[dict]:
        """Find the shortest path between two nodes.

        Args:
            source: Source node ID.
            target: Target node ID.

        Returns:
            Ordered list of nodes and edges forming the shortest path.
        """
        raise NotImplementedError

    async def prune(self) -> list[str]:
        """Remove expired nodes and their edges.

        Returns:
            IDs of pruned nodes.
        """
        raise NotImplementedError
