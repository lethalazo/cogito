# Architecture

## Overview

Cogito is a layered system. Each layer has a single responsibility and communicates through well-defined interfaces.

```
Chat UI → API Layer → Agent Framework → Cognition Layer → Storage
                                      → Identity Layer
```

## Layers

### Chat UI (Frontend)
Next.js application. Sends messages to the API, renders responses. Minimal — the intelligence lives in the backend.

### API Layer
FastAPI server exposing REST endpoints:
- `POST /chat` — Send a message, get a response
- `GET /threads` — List conversation threads
- `GET /threads/{id}` — Get thread history
- `GET /memory` — Query memories
- `POST /memory` — Manually store a memory

### Agent Framework
Agents are the execution units. Each agent has:
- **Identity** — loaded from `SOUL.md` + `config.yaml`
- **Tools** — functions the agent can call (web search, browser, code execution, cognition)
- **Turn lifecycle** — pre-turn (inject context) → LLM call → post-turn (extract and persist)

`BaseAgent` wraps the Anthropic Claude SDK. `CogitoBasic` is the first concrete agent — a general-purpose, cognition-enhanced assistant.

### Cognition Layer
Three storage systems that give the agent persistent intelligence:

| Component | Format | Purpose |
|-----------|--------|---------|
| Memory | JSONL | Short-to-medium term learned state — observations, preferences, inferences |
| Knowledge Base | Markdown + YAML frontmatter | Long-lived structured knowledge — entities, facts, models |
| Knowledge Graph | JSONL (nodes + edges) | Relational understanding — connections, causality, impact chains |

Supporting subsystems:
- **Embeddings** — Voyage AI (voyage-3-lite) for semantic similarity
- **Scoring** — Relevance, recency, accuracy, and impact scoring for memory retrieval
- **Maintenance** — Sleep phase: prune decayed memories, consolidate related ones, update graph

### Identity Layer
Each agent has a `SOUL.md` defining its personality, values, and purpose. Each user has a `profile.yaml` with preferences and context. The identity loader injects these into the agent's system prompt.

## Data Flow

### On each user message:

1. **API** receives message, resolves thread and user context
2. **Thread Manager** loads conversation history
3. **Agent** runs pre-turn:
   - Recall relevant memories (semantic search + scoring)
   - Query knowledge base for relevant entities
   - Query graph for related concepts
   - Load user profile and agent identity
   - Inject all context into system prompt
4. **Agent** calls Claude with enriched context + tools
5. **Claude** responds, potentially calling tools (including cognition tools)
6. **Agent** runs post-turn:
   - Extract new observations, inferences, preferences from the conversation
   - Store new memories
   - Update knowledge base if new entities/facts emerged
   - Update graph if new relationships discovered
7. **API** returns response to frontend

### Sleep phase (periodic maintenance):

1. Score all memories — decay old ones, boost frequently accessed ones
2. Prune memories below threshold
3. Consolidate similar memories into stronger single entries
4. Rebuild graph connections based on updated knowledge
5. Re-index knowledge base embeddings if needed

## Tech Stack Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| LLM | Claude (Anthropic) | Best reasoning, tool use, and instruction following |
| Embeddings | Voyage AI (voyage-3-lite) | High quality, fast, cost-effective |
| Storage | File-based (JSONL, MD) | Simple, portable, no database dependency for MVP |
| Backend | FastAPI + Python | Best ecosystem for AI/ML, async support |
| Frontend | Next.js | Standard React framework, SSR capable |
| Package management | uv | Fast, reliable Python dependency management |

File-based storage is intentional for MVP. It's simple, inspectable, and portable. Database-backed storage is a Phase 2 optimization — the interfaces are designed to make this swap trivial.
