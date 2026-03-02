"""Thread manager — create, retrieve, and manage conversation threads."""

from typing import Any


class ThreadManager:
    """Manages conversation threads and their message history."""

    async def create(self, user_id: str, agent_id: str = "cogito-basic") -> dict[str, Any]:
        """Create a new conversation thread.

        Args:
            user_id: The user who owns this thread.
            agent_id: The agent for this thread.

        Returns:
            The created thread metadata.
        """
        raise NotImplementedError

    async def get(self, thread_id: str) -> dict[str, Any]:
        """Get a thread's metadata and message history.

        Args:
            thread_id: The thread identifier.

        Returns:
            Thread metadata and messages.
        """
        raise NotImplementedError

    async def list(self, user_id: str) -> list[dict[str, Any]]:
        """List all threads for a user.

        Args:
            user_id: The user identifier.

        Returns:
            List of thread summaries.
        """
        raise NotImplementedError

    async def append_message(
        self, thread_id: str, role: str, content: str
    ) -> dict[str, Any]:
        """Append a message to a thread.

        Args:
            thread_id: The thread identifier.
            role: "user" or "assistant".
            content: The message content.

        Returns:
            The appended message.
        """
        raise NotImplementedError
