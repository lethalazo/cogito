"""Cognition tools - recall, persist, and maintain cognitive state.

These tools let the agent explicitly interact with its own cognition layer
during a turn, in addition to the automatic pre-turn/post-turn cognition.

Privacy model:
- User-tier operations require the wallet address and encryption/decryption key
- Shared cognition operations (KB, graph) are public and unencrypted
- The agent never stores user-specific data in shared cognition
"""

from typing import Any

RECALL_TOOL: dict[str, Any] = {
    "name": "cognition_recall",
    "description": "Search memories and knowledge for information relevant to a query.",
    "input_schema": {
        "type": "object",
        "properties": {
            "query": {
                "type": "string",
                "description": "The semantic search query.",
            },
            "tier": {
                "type": "string",
                "enum": ["global", "user", "agent"],
                "description": "Memory tier to search. Defaults to all tiers.",
            },
            "limit": {
                "type": "integer",
                "description": "Maximum number of results. Defaults to 10.",
            },
        },
        "required": ["query"],
    },
}

PERSIST_TOOL: dict[str, Any] = {
    "name": "cognition_persist",
    "description": "Store a new memory or knowledge base entity.",
    "input_schema": {
        "type": "object",
        "properties": {
            "type": {
                "type": "string",
                "enum": ["memory", "kb_entity"],
                "description": "What to persist - a memory or a KB entity.",
            },
            "content": {
                "type": "string",
                "description": "The content to store.",
            },
            "memory_type": {
                "type": "string",
                "enum": ["observation", "inference", "preference", "fact", "episode"],
                "description": "Type of memory (if persisting a memory).",
            },
            "tags": {
                "type": "array",
                "items": {"type": "string"},
                "description": "Tags for categorization.",
            },
        },
        "required": ["type", "content"],
    },
}

MAINTAIN_TOOL: dict[str, Any] = {
    "name": "cognition_maintain",
    "description": "Update or correct existing memories.",
    "input_schema": {
        "type": "object",
        "properties": {
            "memory_id": {
                "type": "string",
                "description": "The ID of the memory to update.",
            },
            "action": {
                "type": "string",
                "enum": ["update_accuracy", "supersede", "delete"],
                "description": "The maintenance action to perform.",
            },
            "new_content": {
                "type": "string",
                "description": "New content (for supersede action).",
            },
            "accuracy_score": {
                "type": "number",
                "description": "New accuracy score (for update_accuracy action).",
            },
        },
        "required": ["memory_id", "action"],
    },
}


async def recall(
    query: str,
    tier: str | None = None,
    limit: int = 10,
    wallet_address: str | None = None,
    decryption_key: bytes | None = None,
) -> list[dict]:
    """Search memories and knowledge by semantic similarity.

    User-tier recall requires wallet_address and decryption_key to access
    encrypted memories.

    Args:
        query: The search query.
        tier: Optional memory tier filter.
        limit: Maximum results to return.
        wallet_address: Wallet address for user-scoped recall.
        decryption_key: AES-256 key for decrypting user-tier memories.

    Returns:
        List of matching memories/entities ranked by score.
    """
    raise NotImplementedError


async def persist(
    type: str,
    content: str,
    memory_type: str | None = None,
    tags: list[str] | None = None,
    wallet_address: str | None = None,
    encryption_key: bytes | None = None,
) -> dict:
    """Store a new memory or KB entity.

    User-tier memories are encrypted with the provided key before storage.
    KB entities are stored unencrypted in shared cognition.

    Args:
        type: "memory" or "kb_entity".
        content: The content to store.
        memory_type: Type of memory (if applicable).
        tags: Tags for categorization.
        wallet_address: Wallet address for user-scoped memories.
        encryption_key: AES-256 key for encrypting user-tier memories.

    Returns:
        The created entry.
    """
    raise NotImplementedError


async def maintain(
    memory_id: str,
    action: str,
    new_content: str | None = None,
    accuracy_score: float | None = None,
    wallet_address: str | None = None,
    encryption_key: bytes | None = None,
) -> dict:
    """Perform maintenance on an existing memory.

    User-tier maintenance requires wallet_address and encryption_key.

    Args:
        memory_id: The memory to maintain.
        action: "update_accuracy", "supersede", or "delete".
        new_content: New content for supersede.
        accuracy_score: New score for update_accuracy.
        wallet_address: Wallet address for user-scoped memories.
        encryption_key: AES-256 key for re-encrypting updated user-tier memories.

    Returns:
        The updated or deleted entry.
    """
    raise NotImplementedError
