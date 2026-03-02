# Cogito

**Autonomous personal superintelligence with persistent memory, a hard knowledge base, and a knowledge graph.**

Cogito is a cognitive AI agent framework. It doesn't just respond — it remembers, learns, and builds a structured understanding of you and the world over time. Every interaction makes it smarter.

> Enterprise version is live internally. This is the open-source consumer version.

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                        Chat UI (Next.js)                        │
└──────────────────────────────┬──────────────────────────────────┘
                               │
┌──────────────────────────────▼──────────────────────────────────┐
│                      API Layer (FastAPI)                         │
│                  /chat  /threads  /memory                        │
└──────────────────────────────┬──────────────────────────────────┘
                               │
┌──────────────────────────────▼──────────────────────────────────┐
│                       Agent Framework                            │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────────┐ │
│  │  BaseAgent   │  │Cogito Basic │  │  Tools                  │ │
│  │  (Claude SDK)│  │ (singleton) │  │  web_search, browser,   │ │
│  │             │  │             │  │  code_exec, cognition   │ │
│  └─────────────┘  └─────────────┘  └─────────────────────────┘ │
└──────────────────────────────┬──────────────────────────────────┘
                               │
┌──────────────────────────────▼──────────────────────────────────┐
│                      Cognition Layer                             │
│  ┌──────────────┐  ┌──────────────┐  ┌───────────────────────┐ │
│  │   Memory      │  │ Knowledge    │  │  Knowledge Graph      │ │
│  │   (JSONL)     │  │ Base (MD)    │  │  (Nodes + Edges)      │ │
│  │              │  │             │  │                       │ │
│  │ observations  │  │ entities     │  │ concepts, entities,   │ │
│  │ inferences    │  │ facts        │  │ relationships,        │ │
│  │ preferences   │  │ models       │  │ cause-effect chains   │ │
│  │ episodes      │  │ scripts      │  │                       │ │
│  └──────────────┘  └──────────────┘  └───────────────────────┘ │
│                                                                  │
│  ┌──────────────┐  ┌──────────────┐  ┌───────────────────────┐ │
│  │  Embeddings   │  │  Scoring     │  │  Maintenance          │ │
│  │  (Voyage AI)  │  │  (relevance, │  │  (sleep phase,        │ │
│  │              │  │  recency,    │  │  prune, consolidate)  │ │
│  │              │  │  accuracy)   │  │                       │ │
│  └──────────────┘  └──────────────┘  └───────────────────────┘ │
└─────────────────────────────────────────────────────────────────┘
                               │
┌──────────────────────────────▼──────────────────────────────────┐
│                      Identity Layer                              │
│              SOUL.md (agent) + profile.yaml (user)               │
└─────────────────────────────────────────────────────────────────┘
```

## Cognitive Components

### Memory (JSONL)
Persistent, scored, multi-tier memory. Memories are observations, inferences, preferences, facts, and episodes — each scored for relevance, accuracy, and impact. Scoped to global, per-user, or per-agent tiers. Old memories decay; important ones consolidate.

### Knowledge Base (Markdown + YAML frontmatter)
Structured, long-lived knowledge. Entities, facts, models, and agent-written scripts stored as Markdown files with typed YAML frontmatter. Indexed with embeddings for semantic search. The agent's hard drive.

### Knowledge Graph (JSONL nodes + edges)
Relational understanding. Typed nodes (concepts, entities, people, assets, events) connected by weighted edges (impacts, causes, related_to, owns). Enables reasoning about connections, second-order effects, and causal chains.

## Quick Start

### Prerequisites
- Python 3.11+
- Node.js 20+
- [uv](https://github.com/astral-sh/uv) (Python package manager)
- Anthropic API key
- Voyage AI API key (for embeddings)

### Backend
```bash
cd backend
uv sync
uv run uvicorn cogito.api.routes:app --reload
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```

## Project Structure

```
cogito/
├── backend/cogito/          # Python backend
│   ├── agent/               # Agent framework (BaseAgent, tools)
│   ├── cognition/           # Memory, KB, Graph, embeddings, scoring
│   ├── identity/            # SOUL.md + user profile loading
│   ├── threads/             # Conversation thread management
│   └── api/                 # FastAPI routes
├── frontend/src/            # Next.js chat UI
├── agents/                  # Agent definitions (SOUL.md + config)
│   └── cogito-basic/        # General-purpose cognition-enhanced agent
├── docs/                    # Architecture, specs, roadmap
└── data/                    # Runtime storage (gitignored)
```

## Tech Stack

| Layer | Technology |
|-------|-----------|
| LLM | Claude (Anthropic SDK) |
| Embeddings | Voyage AI (voyage-3-lite) |
| Backend | Python, FastAPI, Pydantic |
| Frontend | Next.js, React, Tailwind CSS |
| Storage | JSONL (memory, graph), Markdown (KB) |
| Package management | uv (Python), npm (Node) |

## Roadmap

| Phase | Focus | Auth | Privacy |
|-------|-------|------|---------|
| **1 — MVP** | Working cognition layer, Cogito Basic agent, simple tools, chat UI | API key | Centralized |
| **2 — Multi-Agent** | Specialist agents, cross-invocation, adversarial pattern | Wallet-connect | Centralized |
| **3 — Deep Cognition** | World model, second-order effects, cause-effect simulations | Wallet-connect | Client-side encryption |
| **4 — Decentralized** | Cognitive portability, TEE inference, P2P, PAYG via USDC | Wallet-connect | Platform-blind |

Decentralization is progressive: MVP ships centralized → auth decentralizes → data decentralizes → execution decentralizes.

See [docs/roadmap.md](docs/roadmap.md) for the full roadmap.

## License

Apache 2.0 — see [LICENSE](LICENSE).
