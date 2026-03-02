"""Identity loader — load agent definitions and user profiles."""

from pathlib import Path
from typing import Any


async def load_agent(agent_id: str, agents_dir: Path | None = None) -> dict[str, Any]:
    """Load an agent's SOUL.md and config.yaml.

    Args:
        agent_id: The agent identifier (e.g., "cogito-basic").
        agents_dir: Path to agents directory. Defaults to project agents/ dir.

    Returns:
        Dict with "soul" (str) and "config" (dict) keys.
    """
    raise NotImplementedError


async def load_user_profile(user_id: str, users_dir: Path | None = None) -> dict[str, Any]:
    """Load a user's profile.yaml.

    Args:
        user_id: The user identifier.
        users_dir: Path to users data directory.

    Returns:
        The user profile dict.
    """
    raise NotImplementedError


async def create_user(user_id: str, users_dir: Path | None = None) -> dict[str, Any]:
    """Create a new user with default profile.

    Args:
        user_id: The user identifier.
        users_dir: Path to users data directory.

    Returns:
        The created user profile.
    """
    raise NotImplementedError


async def list_agents(agents_dir: Path | None = None) -> list[dict[str, Any]]:
    """List all available agents.

    Args:
        agents_dir: Path to agents directory.

    Returns:
        List of agent summaries (id, name, description).
    """
    raise NotImplementedError
