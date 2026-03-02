# Roadmap

Cogito ships iteratively. Start extremely small, evolve based on real usage.

Decentralization is progressive: MVP ships centralized → auth decentralizes → data decentralizes → execution decentralizes.

---

## Phase 1 — MVP

**Goal:** Working cognition layer + single agent + chat UI. Ship it, then evolve.

### Deliverables
- **Cognition layer** — Memory (JSONL), Knowledge Base (MD), Knowledge Graph (JSONL) with full CRUD operations
- **Embeddings** — Voyage AI (voyage-3-lite) integration for semantic search
- **Scoring** — Relevance/recency/accuracy/impact scoring for memory retrieval
- **Cogito Basic agent** — General-purpose, cognition-enhanced assistant using Claude
- **Tools** — Web search, browser, code execution, cognition (recall/persist/maintain)
- **Turn lifecycle** — Pre-turn context injection, post-turn knowledge extraction
- **API** — FastAPI with /chat, /threads, /memory endpoints
- **Chat UI** — Minimal Next.js frontend for conversations
- **Identity** — SOUL.md for agent personality, profile.yaml for user context

### Architecture
- Centralized deployment
- API key authentication
- File-based storage (JSONL, Markdown)
- Single-user focused

### Non-Goals (Phase 1)
- Multi-agent orchestration
- Encryption or privacy features
- Database-backed storage
- Multi-tenant auth

---

## Phase 2 — Multi-Agent

**Goal:** Specialist agents that can cross-invoke each other.

### Deliverables
- **Agent registry** — Define and manage multiple agents with different specializations
- **Cross-invocation** — Agents can call other agents as tools
- **Adversarial pattern** — Critic/verifier agents that challenge primary agent's outputs
- **Shared cognition** — Agents share the global memory tier, have private agent-tier memories
- **Wallet-connect auth** — Replace API keys with wallet-based authentication
- **Multi-user support** — Per-user memory isolation, user profiles

### Architecture
- Wallet-connect replaces API key auth
- Agent-to-agent communication protocol
- User isolation at the data layer

---

## Phase 3 — Deep Cognition

**Goal:** World model, second-order effects, cause-effect simulations.

### Deliverables
- **World model** — Graph-based model of how entities relate and influence each other
- **Second-order reasoning** — "If X happens, what are the downstream effects?"
- **Cause-effect simulation** — Walk impact chains in the knowledge graph
- **Temporal reasoning** — Understanding trends, cycles, and time-dependent relationships
- **Client-side encryption** — User data encrypted before reaching the server (platform-blind)

### Architecture
- Client-side encryption for user data
- Server cannot read user memories or knowledge
- Richer graph operations (multi-hop traversal, weighted path analysis)

---

## Phase 4 — Decentralized

**Goal:** Cognitive portability, privacy-first execution, peer-to-peer deployment.

### Deliverables
- **Cognitive portability / memory chips** — Export your cognition layer, import into any compatible agent
- **TEE-based inference** — Run LLM inference in Trusted Execution Environments for privacy
- **P2P deployment** — Run Cogito nodes that can discover and communicate with each other
- **PAYG via USDC** — Pay-as-you-go pricing using USDC on Payproof rails
- **Agent marketplace** — Publish and discover agents created by the community

### Architecture
- Fully decentralized execution option
- TEE for inference privacy
- USDC micropayments for compute
- Portable cognition format (standard for memory/KB/graph export)
