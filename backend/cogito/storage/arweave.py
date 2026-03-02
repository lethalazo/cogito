"""Arweave storage backend — permanent, immutable shared cognition.

Shared cognition (knowledge base, knowledge graph, world model) is stored on Arweave
for permanent, censorship-resistant access. This data is public and unencrypted — it's
the agent's world model, containing no user-specific information.

Data is tagged for queryability (entity type, content type, agent ID, etc.) and can be
retrieved by transaction ID or queried via GraphQL on the Arweave gateway.

Self-hosted nodes read shared cognition from Arweave (read-only) — they don't need to
trust any central server for the agent's knowledge.
"""

from typing import Any

from cogito.storage.base import ImmutableStorageBackend


class ArweaveStorage(ImmutableStorageBackend):
    """Arweave-backed immutable storage for shared cognition.

    Data stored here is permanent and public. No encryption — this is the agent's
    world model, not user data. Tagged for GraphQL queryability.

    Requires an Arweave wallet (JWK) for writing. Reading is permissionless.
    """

    def __init__(self, gateway_url: str = "https://arweave.net") -> None:
        self.gateway_url = gateway_url

    async def store(self, key: str, data: bytes, **metadata: Any) -> str:
        """Submit a transaction to Arweave with tagged data.

        Args:
            key: Logical key (stored as a tag for queryability).
            data: Raw bytes to store permanently.
            **metadata: Arweave tags (key-value pairs for GraphQL queries).

        Returns:
            The Arweave transaction ID.
        """
        raise NotImplementedError

    async def retrieve(self, key: str) -> bytes:
        """Fetch data from Arweave by transaction ID.

        Args:
            key: The Arweave transaction ID.

        Returns:
            The stored bytes.
        """
        raise NotImplementedError

    async def list_keys(self, prefix: str = "") -> list[str]:
        """Query Arweave for transaction IDs matching tag patterns.

        Uses Arweave GraphQL to find transactions with matching tags.
        """
        raise NotImplementedError

    async def exists(self, key: str) -> bool:
        """Check if a transaction exists on Arweave."""
        raise NotImplementedError

    async def query_by_tags(self, tags: dict[str, str]) -> list[str]:
        """Query Arweave transactions by tag key-value pairs.

        Uses the Arweave GraphQL endpoint to find matching transactions.

        Args:
            tags: Tag filters (e.g., {"App-Name": "Cogito", "Type": "kb_entity"}).

        Returns:
            List of matching transaction IDs, newest first.
        """
        raise NotImplementedError
