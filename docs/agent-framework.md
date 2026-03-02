# Agent Framework

## Overview

Agents are the execution units of Cogito. Each agent wraps the Anthropic Claude SDK and is enhanced with tools and cognition.

## BaseAgent

`BaseAgent` is the abstract base class for all agents. It handles:
- Loading identity (SOUL.md + config.yaml)
- Managing tools
- Running the turn lifecycle
- Interfacing with the cognition layer

### Interface

```python
class BaseAgent:
    agent_id: str
    soul: str           # Loaded from SOUL.md
    config: AgentConfig  # Loaded from config.yaml
    tools: list[Tool]

    async def run(self, message: str, thread_id: str, user_id: str) -> str:
        """Full turn: pre-turn → LLM → post-turn."""

    async def think(self, message: str, context: TurnContext) -> LLMResponse:
        """Call Claude with enriched context and tools."""

    async def act(self, tool_call: ToolCall) -> ToolResult:
        """Execute a tool call and return the result."""
```

## Turn Lifecycle

Every agent turn follows this sequence:

### 1. Pre-Turn: Inject Context

Before calling the LLM, the agent enriches the conversation with relevant context:

```
Input: user message + thread history
  ↓
Recall relevant memories (semantic search + scoring)
  ↓
Query KB for relevant entities
  ↓
Query graph for related concepts and connections
  ↓
Load user profile (preferences, context)
  ↓
Load agent identity (SOUL.md)
  ↓
Build system prompt with all injected context
  ↓
Output: enriched system prompt + message history + tools
```

### 2. LLM Call

Call Claude via the Anthropic SDK with:
- System prompt (identity + injected context)
- Message history (thread)
- Available tools

Claude may respond with text, tool calls, or both. Tool calls are executed and results fed back in a loop until Claude produces a final text response.

### 3. Post-Turn: Extract and Persist

After the LLM responds, the agent extracts learnings:

```
Input: full conversation turn (user message + agent response)
  ↓
Extract observations ("user mentioned X")
  ↓
Extract inferences ("user likely interested in Y")
  ↓
Extract preferences ("user prefers Z")
  ↓
Identify new entities for KB
  ↓
Identify new relationships for graph
  ↓
Store all extracted knowledge
  ↓
Output: updated cognition state
```

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
| `cognition.recall` | Search memories by semantic query |
| `cognition.persist` | Store a new memory or KB entity |
| `cognition.maintain` | Trigger maintenance on specific memories |

### Cognition Tools

The cognition tools are special — they let the agent explicitly interact with its own cognition layer during a turn. This means Claude can:
- **Recall**: "Let me check what I know about this user's preferences"
- **Persist**: "I should remember that this user works at a crypto startup"
- **Maintain**: "This memory seems outdated, let me update it"

This is in addition to the automatic pre-turn/post-turn cognition that happens on every turn.

## Cogito Basic

Cogito Basic is the first concrete agent. It's a general-purpose, cognition-enhanced assistant.

### Spec

| Property | Value |
|----------|-------|
| ID | `cogito-basic` |
| Model | Claude Sonnet (default) |
| Tools | web_search, browser, code_exec, cognition |
| Identity | General-purpose assistant with persistent memory |
| Constraints | No financial advice, no medical advice, honest about limitations |

### SOUL.md

The SOUL.md file defines the agent's personality, values, and purpose. See `agents/cogito-basic/SOUL.md`.

### config.yaml

The config.yaml file defines the agent's tools, model, and constraints. See `agents/cogito-basic/config.yaml`.

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
