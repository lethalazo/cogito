# Architecture

## Overview

Cogito is a layered, decentralized system. Users interact through a unified interface. Behind it, cognitive agents provide intelligent, memory-enhanced responses. The infrastructure is trustless — wallet-based auth, client-side encryption, and decentralized storage ensure users don't need to trust the platform with their data.

```
Unified Interface → API Layer (SIWE auth) → Cognitive Agents → Cognition Layer → Decentralized Storage (IPFS + Arweave)
```

## Layers

### Unified Interface (Frontend)
A single interface — web and app — for accessing all Cogito agents. Like ChatGPT or Gemini, but with real cognition, real privacy, and no platform lock-in. Users authenticate with their wallet and interact with agents through conversations.

### API Layer
FastAPI server with SIWE wallet authentication:

**Auth endpoints (public):**
- `GET /auth/nonce` — Get a nonce for SIWE authentication
- `POST /auth/verify` — Verify SIWE signature, get JWT session
- `POST /auth/logout` — Revoke session

**Protected endpoints (require wallet session):**
- `POST /chat` — Send a message, get a response
- `GET /threads` — List conversation threads
- `GET /threads/{id}` — Get thread history
- `GET /memory` — Query memories
- `POST /memory` — Store a memory

### Cognitive Agents
Agents are the intelligence layer. Each agent is a singleton service — one agent definition serving all users, with strict per-user data isolation enforced by wallet-based identity and client-side encryption.

Each agent has:
- **Identity** — Personality, values, and purpose (SOUL.md + config)
- **Tools** — Web search, browser, code execution, cognition
- **Turn lifecycle** — Pre-turn (decrypt + inject) → LLM call → post-turn (extract + encrypt)

The internal agent framework (Python) wraps the Anthropic Claude SDK. Users never see the framework — they interact with agents through the unified interface.

### Cognition Layer
Three storage systems that give agents persistent intelligence:

| Component | Storage | Encryption | Scope |
|-----------|---------|------------|-------|
| Memory | IPFS (user-tier) / Arweave (agent/global) | AES-256-GCM (user-tier) | Per-user isolated (user) / Shared (agent, global) |
| Knowledge Base | Arweave | None (public) | Shared world model |
| Knowledge Graph | Arweave | None (public) | Shared world model |

Supporting subsystems:
- **Embeddings** — Dual model: sentence-transformers (private, local) + Voyage AI (public)
- **Scoring** — Relevance, recency, accuracy, and impact scoring for memory retrieval
- **Maintenance** — Sleep phase: prune decayed memories, consolidate related ones, update graph

### Decentralized Infrastructure

| Component | Technology | Purpose |
|-----------|-----------|---------|
| Auth | SIWE (Sign-In with Ethereum) | Trustless wallet-based authentication |
| User storage | IPFS | Encrypted, mutable user data |
| Shared storage | Arweave | Permanent, public world model |
| Encryption | AES-256-GCM + HKDF-SHA256 | Client-side encryption with wallet-derived keys |
| Key management | Lit Protocol | Decentralized access control, no centralized key custodian |
| Payments | USDC on Payproof | Pay-as-you-go for compute |

## Data Flow

### On each user message:

1. **API** receives message, authenticates via SIWE/JWT, resolves session
2. **Thread Manager** loads encrypted conversation history, decrypts in-memory
3. **Agent** runs pre-turn:
   - Fetch encrypted user memories from IPFS → decrypt in-memory
   - Query shared knowledge base from Arweave
   - Query shared graph from Arweave
   - Load encrypted user preferences → decrypt in-memory
   - Inject all context into system prompt
4. **Agent** calls Claude with enriched context + tools
5. **Claude** responds, potentially calling tools (including cognition tools)
6. **Agent** runs post-turn:
   - Extract new observations, inferences, preferences
   - Encrypt user-scoped learnings → store to IPFS
   - Store world knowledge to shared cognition on Arweave (unencrypted)
7. **API** returns response to the interface

### Session data flow (encryption boundaries):

```
[Client]                    [Server]                    [Storage]
   │                           │                            │
   │── wallet signature ──────>│                            │
   │<── JWT session ───────────│                            │
   │                           │                            │
   │── message + JWT ─────────>│── fetch encrypted ────────>│ IPFS
   │                           │<── encrypted blobs ────────│
   │                           │                            │
   │                           │── decrypt in-memory        │
   │                           │── agent processes          │
   │                           │── encrypt new data         │
   │                           │                            │
   │                           │── store encrypted ────────>│ IPFS
   │                           │── store world knowledge ──>│ Arweave
   │                           │                            │
   │<── response ──────────────│                            │
```

### Sleep phase (periodic maintenance):

1. **Shared cognition maintenance** (runs independently):
   - Re-index KB embeddings on Arweave
   - Prune expired graph nodes
   - Strengthen reinforced graph edges

2. **User-tier maintenance** (only during active sessions with key):
   - Recalculate composite scores with updated decay
   - Prune memories below threshold
   - Consolidate similar memories

## Tech Stack Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| LLM | Claude (Anthropic) | Best reasoning, tool use, and instruction following |
| Public embeddings | Voyage AI (voyage-3-lite) | High quality, fast, cost-effective |
| Private embeddings | sentence-transformers (all-MiniLM-L6-v2) | Local model, user data never leaves the server |
| User storage | IPFS | Decentralized, content-addressed, mutable via IPNS |
| Shared storage | Arweave | Permanent, immutable, censorship-resistant |
| Auth | SIWE | Trustless, portable, anonymous, standard (EIP-4361) |
| Encryption | AES-256-GCM + HKDF-SHA256 | Industry standard, authenticated encryption, deterministic key derivation |
| Key management | Lit Protocol | Decentralized, no centralized key custodian |
| Backend | FastAPI + Python | Best ecosystem for AI/ML, async support |
| Frontend | Next.js | Standard React framework, SSR capable |
| Payments | USDC on Payproof | Trustless, on-chain, no payment processor |
