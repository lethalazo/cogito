"""Embedding utilities — dual model for privacy-preserving semantic search.

Two embedding scopes:
- PUBLIC: Voyage AI (voyage-3-lite) — for shared cognition (KB, graph, world model).
  High-quality embeddings via external API. Data is public anyway, so no privacy concern.
- PRIVATE: sentence-transformers (all-MiniLM-L6-v2) — for user-scoped data (memories,
  preferences). Runs locally, no data leaves the server. Embeddings are computed on
  already-decrypted data in memory and are stored encrypted alongside the data.

This dual model ensures user data never touches external embedding APIs.
"""

from enum import Enum

import numpy as np


class EmbeddingScope(Enum):
    """Determines which embedding model to use based on data privacy scope."""

    PRIVATE = "private"  # User-scoped data → local model (sentence-transformers)
    PUBLIC = "public"  # Shared cognition → Voyage AI


async def embed(
    text: str,
    scope: EmbeddingScope = EmbeddingScope.PUBLIC,
    model: str | None = None,
) -> list[float]:
    """Generate an embedding vector for a text string.

    Routes to the appropriate model based on scope:
    - PUBLIC → Voyage AI (voyage-3-lite)
    - PRIVATE → sentence-transformers (all-MiniLM-L6-v2), runs locally

    Args:
        text: The text to embed.
        scope: Privacy scope determining which model to use.
        model: Override the default model for the scope.

    Returns:
        The embedding vector.
    """
    raise NotImplementedError


async def batch_embed(
    texts: list[str],
    scope: EmbeddingScope = EmbeddingScope.PUBLIC,
    model: str | None = None,
) -> list[list[float]]:
    """Generate embeddings for multiple texts.

    Routes to the appropriate model based on scope.

    Args:
        texts: The texts to embed.
        scope: Privacy scope determining which model to use.
        model: Override the default model for the scope.

    Returns:
        List of embedding vectors.
    """
    raise NotImplementedError


def similarity(a: list[float], b: list[float]) -> float:
    """Compute cosine similarity between two embedding vectors.

    Args:
        a: First embedding vector.
        b: Second embedding vector.

    Returns:
        Cosine similarity score (0.0 to 1.0).
    """
    a_arr = np.array(a)
    b_arr = np.array(b)
    dot = np.dot(a_arr, b_arr)
    norm = np.linalg.norm(a_arr) * np.linalg.norm(b_arr)
    if norm == 0:
        return 0.0
    return float(dot / norm)
