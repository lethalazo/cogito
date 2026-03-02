"""Cogito Basic — general-purpose cognition-enhanced agent."""

from cogito.agent.base import BaseAgent


class CogitoBasic(BaseAgent):
    """The default Cogito agent.

    A general-purpose, cognition-enhanced assistant that uses persistent memory,
    a knowledge base, and a knowledge graph to provide contextual, personalized responses.

    This is a singleton agent — one instance per deployment, serving all users
    with wallet-based identity and client-side encryption for per-user data isolation.
    """

    def __init__(self) -> None:
        super().__init__(agent_id="cogito-basic")

    async def run(self, message: str, thread_id: str, wallet_address: str) -> str:
        """Execute a full turn with cognition-enhanced context."""
        raise NotImplementedError
