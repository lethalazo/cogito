"""Thread manager — create, retrieve, and manage conversation threads.

Threads are user-scoped data — stored encrypted on IPFS (or local storage for
self-hosted nodes). Only the wallet holder can access their threads.
"""

from typing import Any

from cogito.storage.base import StorageBackend


class ThreadManager:
    """Manages conversation threads and their message history.

    Uses a StorageBackend for persistence. Thread data is encrypted client-side
    before storage — the platform never sees plaintext conversation history.
    """

    def __init__(self, storage: StorageBackend) -> None:
        self.storage = storage

    async def create(
        self,
        wallet_address: str,
        agent_id: str = "cogito-basic",
        encryption_key: bytes | None = None,
    ) -> dict[str, Any]:
        """Create a new conversation thread.

        Args:
            wallet_address: The wallet address that owns this thread.
            agent_id: The agent for this thread.
            encryption_key: AES-256 key for encrypting thread data.

        Returns:
            The created thread metadata.
        """
        raise NotImplementedError

    async def get(
        self,
        thread_id: str,
        decryption_key: bytes | None = None,
    ) -> dict[str, Any]:
        """Get a thread's metadata and message history.

        Args:
            thread_id: The thread identifier.
            decryption_key: AES-256 key for decrypting thread data.

        Returns:
            Thread metadata and messages.
        """
        raise NotImplementedError

    async def list(
        self,
        wallet_address: str,
        decryption_key: bytes | None = None,
    ) -> list[dict[str, Any]]:
        """List all threads for a wallet.

        Args:
            wallet_address: The wallet address.
            decryption_key: AES-256 key for decrypting thread metadata.

        Returns:
            List of thread summaries.
        """
        raise NotImplementedError

    async def append_message(
        self,
        thread_id: str,
        role: str,
        content: str,
        encryption_key: bytes | None = None,
    ) -> dict[str, Any]:
        """Append a message to a thread.

        The message is encrypted before storage.

        Args:
            thread_id: The thread identifier.
            role: "user" or "assistant".
            content: The message content.
            encryption_key: AES-256 key for encrypting the message.

        Returns:
            The appended message.
        """
        raise NotImplementedError
