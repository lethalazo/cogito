"""Embedding utilities — Voyage AI integration for semantic search."""

import numpy as np


async def embed(text: str, model: str = "voyage-3-lite") -> list[float]:
    """Generate an embedding vector for a text string.

    Args:
        text: The text to embed.
        model: The Voyage AI model to use.

    Returns:
        The embedding vector.
    """
    raise NotImplementedError


async def batch_embed(texts: list[str], model: str = "voyage-3-lite") -> list[list[float]]:
    """Generate embeddings for multiple texts in a single API call.

    Args:
        texts: The texts to embed.
        model: The Voyage AI model to use.

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
