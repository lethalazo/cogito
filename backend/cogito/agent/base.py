"""Base agent class wrapping the Anthropic Claude SDK.

Agents are singleton services - one definition serving all users, with strict per-user
data isolation enforced by wallet-based identity and client-side encryption.

Turn lifecycle with encryption boundaries:
1. Pre-turn: Fetch encrypted user data → decrypt in-memory → inject context
2. LLM call: Claude processes with decrypted context (in-memory only)
3. Post-turn: Extract learnings → encrypt user data → store to IPFS/local
"""

from dataclasses import dataclass, field
from typing import Any


@dataclass
class AgentConfig:
    """Agent configuration loaded from config.yaml."""

    agent_id: str = ""
    name: str = ""
    description: str = ""
    model: str = "claude-sonnet-4-20250514"
    max_tokens: int = 8192
    tools: list[str] = field(default_factory=list)
    system_prompt_hints: list[str] = field(default_factory=list)
    constraints: list[str] = field(default_factory=list)


@dataclass
class TurnContext:
    """Context assembled for a single agent turn.

    User-scoped data (memories, profile) is decrypted in-memory for the duration
    of the turn and never persisted in plaintext.
    """

    thread_id: str = ""
    wallet_address: str = ""
    encryption_key: bytes = b""
    memories: list[dict] = field(default_factory=list)
    kb_entities: list[dict] = field(default_factory=list)
    graph_context: list[dict] = field(default_factory=list)
    user_profile: dict = field(default_factory=dict)
    system_prompt: str = ""


@dataclass
class ToolCall:
    """A tool call from the LLM."""

    id: str = ""
    name: str = ""
    input: dict = field(default_factory=dict)


@dataclass
class ToolResult:
    """Result of executing a tool call."""

    tool_call_id: str = ""
    content: str = ""
    is_error: bool = False


class BaseAgent:
    """Abstract base agent wrapping the Anthropic Claude SDK.

    Handles identity loading, tool management, and the turn lifecycle
    (pre-turn context injection → LLM call → post-turn extraction).

    Encryption boundaries:
    - Pre-turn: encrypted user data fetched from storage, decrypted in-memory
    - During turn: agent processes with decrypted data (never persisted as plaintext)
    - Post-turn: new user learnings encrypted before storage
    """

    def __init__(self, agent_id: str) -> None:
        self.agent_id = agent_id
        self.soul: str = ""
        self.config: AgentConfig = AgentConfig()
        self.tools: list[dict[str, Any]] = []

    async def run(self, message: str, thread_id: str, wallet_address: str) -> str:
        """Execute a full turn: pre-turn → LLM → post-turn.

        Args:
            message: The user's message.
            thread_id: The conversation thread ID.
            wallet_address: The user's authenticated wallet address.

        Returns:
            The agent's response text.
        """
        raise NotImplementedError

    async def think(self, message: str, context: TurnContext) -> dict:
        """Call Claude with enriched context and tools.

        Args:
            message: The user's message.
            context: Pre-assembled turn context (user data already decrypted).

        Returns:
            The LLM response.
        """
        raise NotImplementedError

    async def act(self, tool_call: ToolCall) -> ToolResult:
        """Execute a tool call and return the result.

        Args:
            tool_call: The tool call to execute.

        Returns:
            The tool execution result.
        """
        raise NotImplementedError

    async def _pre_turn(
        self, message: str, thread_id: str, wallet_address: str
    ) -> TurnContext:
        """Assemble context for a turn.

        Fetches encrypted user data from storage, decrypts in-memory,
        queries shared cognition (KB, graph), and builds the turn context.
        """
        raise NotImplementedError

    async def _post_turn(self, message: str, response: str, context: TurnContext) -> None:
        """Extract and persist learnings from the completed turn.

        User-scoped learnings are encrypted before storage.
        World knowledge goes to shared cognition (unencrypted).
        """
        raise NotImplementedError
