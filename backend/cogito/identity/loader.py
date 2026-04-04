"""Identity loader - load agent definitions and user profiles.

Agent definitions (SOUL.md, config.yaml) are our code - loaded from the filesystem.
User profiles are user-scoped data - stored encrypted on the user's storage backend.
"""

from pathlib import Path
from typing import Any

from cogito.storage.base import StorageBackend


async def load_agent(agent_id: str, agents_dir: Path | None = None) -> dict[str, Any]:
    """Load an agent's SOUL.md and config.yaml.

    Agent definitions are our code, not user data. Loaded from the local filesystem.

    Args:
        agent_id: The agent identifier (e.g., "cogito-basic").
        agents_dir: Path to agents directory. Defaults to project agents/ dir.

    Returns:
        Dict with "soul" (str) and "config" (dict) keys.
    """
    raise NotImplementedError


async def load_user_profile(
    wallet_address: str,
    storage: StorageBackend,
    decryption_key: bytes,
) -> dict[str, Any]:
    """Load a user's profile from their encrypted storage.

    Args:
        wallet_address: The user's wallet address.
        storage: The user's storage backend (IPFS or local).
        decryption_key: AES-256 key for decrypting the profile.

    Returns:
        The decrypted user profile dict.
    """
    raise NotImplementedError


async def create_user(
    wallet_address: str,
    storage: StorageBackend,
    encryption_key: bytes,
) -> dict[str, Any]:
    """Create a new user with default profile, stored encrypted.

    Args:
        wallet_address: The user's wallet address.
        storage: The user's storage backend (IPFS or local).
        encryption_key: AES-256 key for encrypting the profile.

    Returns:
        The created user profile.
    """
    raise NotImplementedError


async def list_agents(agents_dir: Path | None = None) -> list[dict[str, Any]]:
    """List all available agents.

    Agent definitions are our code. Loaded from the local filesystem.

    Args:
        agents_dir: Path to agents directory.

    Returns:
        List of agent summaries (id, name, description).
    """
    raise NotImplementedError
