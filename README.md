# Cogito

**Trustless, decentralized cognitive AI - with persistent memory, a hard knowledge base, and a knowledge graph.**

Cogito is a cognitive AI agent that doesn't just respond - it remembers, learns, and builds a structured understanding of you and the world over time. Every interaction makes it smarter. Your data stays yours - encrypted client-side, stored on IPFS, accessible only by your wallet. The agent's world model lives on Arweave - permanent, public, and permissionless.

Access Cogito through a unified interface - browser and app - like ChatGPT or Gemini, but with real cognition, real privacy, and no platform lock-in.

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                   Unified Interface (Web + App)                  │
└──────────────────────────────┬──────────────────────────────────┘
                               │
┌──────────────────────────────▼──────────────────────────────────┐
│                      API Layer (FastAPI)                         │
│          /auth/nonce  /auth/verify  /chat  /threads  /memory     │
│              SIWE wallet auth · JWT sessions                     │
└──────────────────────────────┬──────────────────────────────────┘
                               │
┌──────────────────────────────▼──────────────────────────────────┐
│                       Cognitive Agents                            │
│  ┌─────────────────────────────────────────────────────────────┐ │
│  │  Cogito Basic (general-purpose)                             │ │
│  │  + future specialist agents                                 │ │
│  └─────────────────────────────────────────────────────────────┘ │
│  Tools: web search, browser, code execution, cognition           │
└──────────────────────────────┬──────────────────────────────────┘
                               │
┌──────────────────────────────▼──────────────────────────────────┐
│                      Cognition Layer                             │
│  ┌──────────────┐  ┌──────────────┐  ┌───────────────────────┐ │
│  │   Memory      │  │ Knowledge    │  │  Knowledge Graph      │ │
│  │  (encrypted)  │  │ Base         │  │  (Nodes + Edges)      │ │
│  │              │  │ (public)     │  │  (public)             │ │
│  │ observations  │  │ entities     │  │ concepts, entities,   │ │
│  │ inferences    │  │ facts        │  │ relationships,        │ │
│  │ preferences   │  │ models       │  │ cause-effect chains   │ │
│  │ episodes      │  │ scripts      │  │                       │ │
│  └──────────────┘  └──────────────┘  └───────────────────────┘ │
│                                                                  │
│  ┌──────────────┐  ┌──────────────┐  ┌───────────────────────┐ │
│  │  Embeddings   │  │  Scoring     │  │  Maintenance          │ │
│  │ Private:      │  │  (relevance, │  │  (sleep phase,        │ │
│  │  sentence-    │  │  recency,    │  │  prune, consolidate)  │ │
│  │  transformers │  │  accuracy)   │  │                       │ │
│  │ Public:       │  │              │  │                       │ │
│  │  Voyage AI    │  │              │  │                       │ │
│  └──────────────┘  └──────────────┘  └───────────────────────┘ │
└─────────────────────────────────────────────────────────────────┘
                               │
┌──────────────────────────────▼──────────────────────────────────┐
│                   Decentralized Infrastructure                   │
│  ┌──────────┐  ┌──────────┐  ┌───────────┐  ┌──────────────┐  │
│  │   SIWE    │  │   IPFS    │  │  Arweave   │  │ Lit Protocol │  │
│  │  wallet   │  │ encrypted │  │  permanent │  │ decentralized│  │
│  │   auth    │  │ user data │  │ world model│  │ key mgmt     │  │
│  └──────────┘  └──────────┘  └───────────┘  └──────────────┘  │
│                                                                  │
│  ┌──────────────────┐  ┌─────────────────────────────────────┐  │
│  │  USDC Payments    │  │  Client-side AES-256-GCM Encryption │  │
│  │  (Payproof rails) │  │  (wallet-derived keys via HKDF)     │  │
│  └──────────────────┘  └─────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
```

## What Makes Cogito Different

| Traditional AI chatbots | Cogito |
|------------------------|--------|
| Stateless - forgets everything | Persistent memory across conversations |
| No real understanding | Knowledge base + knowledge graph = structured world model |
| Platform lock-in | Decentralized - IPFS + Arweave, no single point of failure |
| Centralized trust | Client-side encryption, wallet auth - platform never sees your data |
| One-size-fits-all | Learns your preferences, adapts to you specifically |
| Centralized identity | Wallet-based identity - anonymous, portable, self-sovereign |

## Privacy Model

Two data scopes with strict separation:

| Scope | Storage | Encryption | Embeddings |
|-------|---------|------------|------------|
| **User data** (memories, preferences, threads) | IPFS (mutable, pinned) | AES-256-GCM, wallet-derived key | sentence-transformers (local, private) |
| **Shared cognition** (KB, graph, world model) | Arweave (permanent) | None (public) | Voyage AI |

User data is encrypted client-side before reaching the server. The platform never sees plaintext. See [docs/privacy-model.md](docs/privacy-model.md) for the full privacy model and threat model.

## Quick Start

### Prerequisites
- Python 3.11+
- Node.js 20+
- [uv](https://github.com/astral-sh/uv) (Python package manager)
- Anthropic API key
- Voyage AI API key (for public embeddings)

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
│   ├── agent/               # Agent runtime (internal framework)
│   ├── api/                 # FastAPI routes (SIWE auth + protected endpoints)
│   ├── auth/                # Wallet authentication (SIWE + JWT sessions)
│   ├── cognition/           # Memory, KB, Graph, embeddings, scoring
│   ├── crypto/              # AES-256-GCM encryption, wallet-derived keys, Lit Protocol
│   ├── identity/            # Agent identity + user profile loading
│   ├── payments/            # USDC payments via Payproof
│   ├── storage/             # Decentralized storage (IPFS, Arweave, local)
│   └── threads/             # Conversation thread management
├── frontend/src/            # Unified web interface
├── agents/                  # Agent definitions (identity + config)
│   └── cogito-basic/        # General-purpose cognitive agent
└── docs/                    # Architecture, specs, privacy model, roadmap
```

## Tech Stack

| Layer | Technology |
|-------|-----------|
| LLM | Claude (Anthropic SDK) |
| Embeddings (public) | Voyage AI (voyage-3-lite) |
| Embeddings (private) | sentence-transformers (all-MiniLM-L6-v2) |
| Backend | Python, FastAPI, Pydantic |
| Frontend | Next.js, React, Tailwind CSS |
| Auth | SIWE (Sign-In with Ethereum) + JWT sessions |
| Encryption | AES-256-GCM, HKDF-SHA256, Lit Protocol |
| User storage | IPFS (encrypted, mutable) |
| Shared storage | Arweave (permanent, public) |
| Payments | USDC on Payproof rails |
| Package management | uv (Python), npm (Node) |

## Roadmap

| Phase | Focus |
|-------|-------|
| **1 - MVP** | Working cognition layer, wallet auth (SIWE), client-side encryption, IPFS user storage, Arweave shared cognition, dual embeddings, unified web interface |
| **2 - Specialist Agents** | Domain-specific agents, agent switching, cross-agent cognition |
| **3 - Deep Cognition** | World model, second-order effects, cause-effect simulations |
| **4 - Self-Hosted** | Self-hosted Cogito nodes, cognitive portability, P2P deployment, USDC payments |

See [docs/roadmap.md](docs/roadmap.md) for the full roadmap.

## Docs

- [Architecture](docs/architecture.md) - System layers, data flow, tech stack
- [Cognition Layer](docs/cognition-layer.md) - Memory, KB, Graph, scoring, maintenance
- [Privacy Model](docs/privacy-model.md) - Encryption, key derivation, threat model
- [Decentralization](docs/decentralization.md) - SIWE, IPFS, Arweave, Lit Protocol, self-hosted
- [Agent Framework](docs/agent-framework.md) - Internal agent runtime (BaseAgent, tools, turn lifecycle)
- [Roadmap](docs/roadmap.md) - Development phases

## License

Apache 2.0 - see [LICENSE](LICENSE).
