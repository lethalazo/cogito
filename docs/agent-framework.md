# Agent Framework (Internal)

> This document describes the internal agent framework used to build and maintain Cogito's cognitive agents. Users interact with agents through the unified interface — they never see or interact with the framework directly.

## Overview

The agent framework is the internal Python tooling we use to build, test, and deploy Cogito's cognitive agents. Each agent is a singleton service — one agent definition serving all users, with wallet-based identity and client-side encryption for per-user data isolation.

## BaseAgent

`BaseAgent` is the abstract base class for all agents. It handles:
- Loading identity (SOUL.md + config)
- Managing tools
- Running the turn lifecycle with encryption boundaries
- Interfacing with the cognition layer

### Interface

```python
class BaseAgent:
    agent_id: str
    soul: str           # Loaded from SOUL.md
    config: AgentConfig  # Loaded from config
    tools: list[Tool]

    async def run(self, message: str, thread_id: str, wallet_address: str) -> str:
        """Full turn: pre-turn → LLM → post-turn."""

    async def think(self, message: str, context: TurnContext) -> LLMResponse:
        """Call Claude with enriched context and tools."""

    async def act(self, tool_call: ToolCall) -> ToolResult:
        """Execute a tool call and return the result."""
```

## Turn Lifecycle

Every agent turn follows this sequence, with strict encryption boundaries:

### 1. Pre-Turn: Decrypt + Inject Context

Before calling the LLM, the agent fetches and decrypts user data:

```
Input: user message + thread history + wallet_address
  ↓
Fetch encrypted user memories from IPFS → decrypt in-memory
  ↓
Query shared KB from Arweave (public, no decryption needed)
  ↓
Query shared graph from Arweave (public)
  ↓
Fetch encrypted user preferences from IPFS → decrypt in-memory
  ↓
Load agent identity (SOUL.md)
  ↓
Build system prompt with all injected context
  ↓
Output: TurnContext (wallet_address, encryption_key, decrypted data)
```

### 2. LLM Call

Call Claude via the Anthropic SDK with:
- System prompt (identity + injected context, user data decrypted in-memory)
- Message history (thread)
- Available tools

Claude may respond with text, tool calls, or both. Tool calls are executed and results fed back in a loop until Claude produces a final text response.

### 3. Post-Turn: Extract + Encrypt

After the LLM responds, the agent extracts and persists learnings:

```
Input: full conversation turn (user message + agent response)
  ↓
Extract observations ("user mentioned X") → encrypt → store on IPFS (user-scoped)
  ↓
Extract inferences ("user likely interested in Y") → encrypt → store on IPFS
  ↓
Extract preferences ("user prefers Z") → encrypt → store on IPFS
  ↓
Identify new world knowledge → store on Arweave (shared, unencrypted)
  ↓
Identify new relationships → store on Arweave (shared, unencrypted)
  ↓
Output: updated cognition state
```

**Key principle:** User-specific learnings are encrypted and stored on IPFS. World knowledge goes to Arweave (public, unencrypted). User data never enters shared cognition.

## Tool System

Tools are functions that agents can call during a turn. Each tool has:
- A name and description (for Claude's tool use)
- An input schema (JSON Schema)
- An execute function

### Built-in Tools

| Tool | Description |
|------|-------------|
| `web_search` | Search the web for information |
| `browser` | Navigate to a URL and extract content |
| `code_exec` | Execute Python code in a sandbox |
| `cognition.recall` | Search memories by semantic query (encryption-aware) |
| `cognition.persist` | Store a new memory or KB entity (encryption-aware) |
| `cognition.maintain` | Trigger maintenance on specific memories (encryption-aware) |

### Cognition Tools

The cognition tools are encryption-aware — user-tier operations require the wallet address and encryption/decryption key from the TurnContext:
- **Recall**: Fetches encrypted user memories → decrypts in-memory → returns results
- **Persist**: Encrypts user-tier content → stores on IPFS
- **Maintain**: Decrypts → updates → re-encrypts → stores

Shared cognition operations (KB writes, graph updates) are unencrypted.

## Cogito Basic

Cogito Basic is the first cognitive agent. General-purpose, cognition-enhanced, privacy-preserving.

### Spec

| Property | Value |
|----------|-------|
| ID | `cogito-basic` |
| Model | Claude Sonnet (default) |
| Tools | web_search, browser, code_exec, cognition |
| Identity | General-purpose cognitive assistant |
| Privacy | Never stores user data in shared cognition |
| Constraints | No financial advice, no medical advice, honest about limitations |

## Claude SDK Integration

Agents use the Anthropic Python SDK (`anthropic` package) for LLM calls:

```python
import anthropic

client = anthropic.Anthropic()

response = client.messages.create(
    model=config.model,
    max_tokens=config.max_tokens,
    system=system_prompt,
    messages=messages,
    tools=tools,
)
```

Tool results are fed back in a loop:

```python
while response.stop_reason == "tool_use":
    tool_results = await execute_tool_calls(response.content)
    messages.append({"role": "assistant", "content": response.content})
    messages.append({"role": "user", "content": tool_results})
    response = client.messages.create(...)
```
