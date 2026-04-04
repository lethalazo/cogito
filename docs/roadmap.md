# Roadmap

Cogito ships iteratively. Start small, evolve based on real usage.

Decentralization and trustlessness are built into Phase 1 - not deferred, not bolted on later.

---

## Phase 1 - MVP

**Goal:** Trustless, decentralized cognitive AI accessible through a unified interface. Privacy-preserving from day one.

### Deliverables
- **Unified interface** - Web app for accessing Cogito agents (like ChatGPT/Gemini, but with cognition and privacy)
- **Cogito Basic agent** - General-purpose, cognition-enhanced assistant using Claude
- **Cognition layer** - Memory, Knowledge Base, Knowledge Graph with full CRUD
- **SIWE wallet auth** - Sign-In with Ethereum, no passwords, no emails, no centralized identity
- **Client-side encryption** - AES-256-GCM with wallet-derived keys (HKDF-SHA256)
- **IPFS user storage** - Encrypted user data on IPFS, mutable via IPNS
- **Arweave shared cognition** - Permanent, public world model on Arweave
- **Lit Protocol key management** - Decentralized access control, no centralized key custodian
- **Dual embeddings** - Voyage AI for public data, sentence-transformers for private user data
- **Scoring** - Relevance/recency/accuracy/impact scoring for memory retrieval
- **Tools** - Web search, browser, code execution, cognition (recall/persist/maintain)
- **Turn lifecycle** - Pre-turn decrypt + inject, post-turn extract + encrypt
- **API** - FastAPI with SIWE auth endpoints + protected /chat, /threads, /memory

### Architecture
- Wallet-based authentication (SIWE + JWT sessions)
- Client-side AES-256-GCM encryption for all user-scoped data
- IPFS for encrypted user data, Arweave for public shared cognition
- Dual embedding model (private local + public API)
- Agents are singleton services - one definition, all users, strict cryptographic isolation

### What "trustless" means in MVP
- You authenticate with your wallet - no centralized identity provider
- Your data is encrypted client-side - the platform never sees plaintext
- Encryption keys are derived from your wallet signature - only you can decrypt
- Shared cognition is on Arweave - permanent, censorship-resistant, permissionless
- Key management via Lit Protocol - no centralized key custodian to trust

---

## Phase 2 - Specialist Agents

**Goal:** Domain-specific cognitive agents, all accessible through the same unified interface.

### Deliverables
- **Specialist agents** - Purpose-built agents for research, code, finance, etc.
- **Agent switching** - Seamlessly switch between agents in the interface
- **Cross-agent cognition** - Agents share the same world model (KB + graph) and can build on each other's knowledge
- **Agent-to-agent invocation** - Specialist agents can call other agents as tools
- **Adversarial pattern** - Critic/verifier agents that challenge primary agent's outputs

### Architecture
- Same unified interface, multiple agents behind it
- Agents share public cognition on Arweave, respect user-tier encryption
- Agent-to-agent communication protocol

---

## Phase 3 - Deep Cognition

**Goal:** World model, second-order effects, cause-effect simulations.

### Deliverables
- **World model** - Rich graph-based model of how entities relate and influence each other
- **Second-order reasoning** - "If X happens, what are the downstream effects?"
- **Cause-effect simulation** - Walk impact chains in the knowledge graph
- **Temporal reasoning** - Understanding trends, cycles, and time-dependent relationships
- **Richer graph operations** - Multi-hop traversal, weighted path analysis

### Architecture
- Enhanced cognition layer with deeper graph algorithms
- Simulation engine for cause-effect chains
- Improved maintenance/sleep phase for world model evolution

---

## Phase 4 - Self-Hosted Nodes

**Goal:** Users can host their own Cogito nodes. Cognitive portability. Full decentralization.

### Deliverables
- **Self-hosted Cogito** - Users run their own Cogito node
- **Read-only Arweave** - Self-hosted nodes read shared cognition from Arweave
- **Local user storage** - Keep encrypted user data on your own infrastructure
- **Cognitive portability** - Export your cognition, import into any Cogito node
- **TEE-based inference** - Run LLM inference in Trusted Execution Environments
- **P2P deployment** - Cogito nodes discover and communicate with each other
- **USDC payments** - Pay-as-you-go pricing via USDC on Payproof rails

### Architecture
- Fully decentralized execution option
- TEE for inference privacy
- USDC micropayments for compute
- Portable cognition format (standard for memory/KB/graph export)
- Simple, productized self-hosting experience
