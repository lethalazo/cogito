# Cogito

> **Documentation-Driven Development**: A task is NOT done until docs are updated.

## What This Is

Cogito is a **trustless, decentralized cognitive AI framework** with persistent memory, privacy-first architecture, and wallet-based identity. Three differentiators:

1. **Persistent Memory** - learns and remembers across conversations via a cognition layer (memory, knowledge base, knowledge graph)
2. **Decentralized Architecture** - no platform lock-in; SIWE wallet auth, client-side encryption, IPFS for user data, Arweave for shared knowledge
3. **Privacy by Architecture** - user data encrypted client-side with wallet-derived keys (AES-256-GCM + HKDF-SHA256); server never sees plaintext

**Status**: Active - Phase 1 MVP

## Dev Commands

```bash
# Backend
cd backend
uv sync                                        # Install dependencies
uv run uvicorn cogito.api.routes:app --reload   # Run API server
uv run pytest tests/                            # Run tests
uv run ruff check cogito/                       # Lint

# Frontend
cd frontend
npm install
npm run dev                                     # Dev server (localhost:3000)
npm run build && npm start                      # Production build
npm run lint
```

## Architecture

```
Client (Next.js) ──► FastAPI ──► Cognition Layer ──► Storage
                         │              │                ├── IPFS (encrypted user data)
                         │              │                └── Arweave (public shared knowledge)
                         │              ├── Memory (recall, store, prune, consolidate)
                         │              ├── Knowledge Base (structured world knowledge)
                         │              └── Knowledge Graph (typed nodes + weighted edges)
                         │
                         ├── Auth (SIWE + JWT sessions)
                         ├── Crypto (AES-256-GCM, wallet-derived keys)
                         ├── Agent Framework (BaseAgent → CogitoBasic)
                         └── Payments (Payproof integration)
```

- **Auth**: SIWE (Sign-In with Ethereum) → JWT sessions
- **Encryption**: AES-256-GCM with HKDF-SHA256 key derivation from wallet signatures
- **Storage**: IPFS (mutable, encrypted user data) + Arweave (permanent, public shared cognition)
- **Embeddings**: Dual model - sentence-transformers (local, private) + Voyage AI (public)
- **LLM**: Claude via Anthropic SDK

## Project Structure

```
backend/cogito/
  api/routes.py          # FastAPI entry point
  auth/                  # SIWE, JWT sessions, middleware
  crypto/                # AES-256-GCM encryption, key derivation, Lit Protocol
  cognition/             # Memory, KnowledgeBase, Graph, embeddings, scoring, maintenance
  storage/               # Abstract backends: IPFS, Arweave, local
  agent/                 # BaseAgent, CogitoBasic, tools (web_search, browser, code_exec, cognition)
  identity/              # Agent identity loader, user profiles
  payments/              # Payproof USDC integration
  config.py              # Settings (Pydantic)

agents/cogito-basic/     # Agent definition (SOUL.md + config.yaml)

frontend/src/app/        # Next.js 15 + React 19 + Tailwind
  layout.tsx, page.tsx   # Chat interface (minimal MVP)

docs/                    # Architecture, cognition layer, privacy model, decentralization, agent framework, roadmap
```

## Privacy Model - Two Data Scopes

| Scope | What | Storage | Encryption | Embeddings |
|-------|------|---------|------------|------------|
| **User-scoped** | Memories (user-tier), preferences, threads, profile | IPFS (pinned) | AES-256-GCM (wallet-derived key) | sentence-transformers (local) |
| **Shared cognition** | KB entities, graph, agent/global memories | Arweave (permanent) | None (public) | Voyage AI (external) |

**Rules**:
- User-scoped data NEVER enters shared cognition
- Server never sees plaintext user data or encryption keys
- Per-wallet isolation: each user has a separate IPFS store
- Key derivation: deterministic from wallet signature via HKDF-SHA256

## Key Patterns

- **Cognition layer**: Memory (scored, pruned, consolidated) + KB (Markdown + YAML frontmatter) + Graph (typed nodes: concept/entity/asset/person/stock/file/event, weighted edges)
- **Memory scoring**: `score = 0.4*relevance + 0.25*accuracy + 0.2*impact - 0.15*decay(age)`
- **Agent turn lifecycle**: Pre-turn (decrypt + inject context) → LLM call (Claude + tools) → Post-turn (extract + encrypt + store)
- **Agent definitions**: `SOUL.md` (identity/personality) + `config.yaml` (model, tools, constraints)
- **Payproof integration**: `backend/cogito/payments/usdc.py` - on-chain USDC payment verification

## Code Style

- Python 3.14+, type hints everywhere
- Pydantic v2 for config and validation
- ruff for linting (line-length 100)
- pytest + pytest-asyncio for tests
- Async/await for all I/O
- Dataclasses for domain objects
- Abstract base classes for interfaces (StorageBackend, BaseAgent)

## Environment Variables

**Required**:
```
ANTHROPIC_API_KEY=sk-...
VOYAGE_API_KEY=...
JWT_SECRET=...
```

**Optional**:
```
IPFS_API_URL=/ip4/127.0.0.1/tcp/5001
ARWEAVE_GATEWAY_URL=https://arweave.net
ARWEAVE_WALLET_PATH=./arweave-wallet.json
PAYPROOF_API_URL=https://payproof.io/api
USDC_CONTRACT_ADDRESS=0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48
CHAIN_ID=1
```

## Documentation

- `docs/architecture.md` - System layers, API routes, tech stack decisions
- `docs/cognition-layer.md` - Memory, KB, Graph, embeddings, temporal model, sleep phase
- `docs/privacy-model.md` - Two data scopes, encryption, threat model
- `docs/decentralization.md` - SIWE, IPFS + Arweave, wallet-derived keys, self-hosted nodes
- `docs/agent-framework.md` - BaseAgent, turn lifecycle, tool system, Claude SDK integration
- `docs/roadmap.md` - Phase 1 (MVP) → Phase 2 (Specialists) → Phase 3 (Deep Cognition) → Phase 4 (Self-Hosted)
