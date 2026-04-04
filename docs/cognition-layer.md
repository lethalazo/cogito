# Cognition Layer

The cognition layer is what makes Cogito more than a chatbot. It provides persistent memory, structured knowledge, and relational understanding across conversations.

## Privacy Boundaries

The cognition layer enforces strict privacy boundaries between two data scopes:

| Scope | Components | Storage | Encryption | Embeddings |
|-------|-----------|---------|------------|------------|
| **User-scoped** | User-tier memories, preferences, threads | IPFS (mutable) | AES-256-GCM, wallet-derived key | sentence-transformers (local) |
| **Shared cognition** | KB, graph, agent/global memories | Arweave (permanent) | None (public) | Voyage AI |

**User data never enters shared cognition.** This is enforced at the architecture level - user-scoped data flows through encrypted storage, while shared cognition flows through public storage.

## Three Cognitive Components

| Component | Storage | Analogy | Lifespan | Scope |
|-----------|---------|---------|----------|-------|
| **Memory** | IPFS (user) / Arweave (shared) | Working memory / episodic memory | Short-to-medium term, decays | Per-user isolated + per-agent shared |
| **Knowledge Base** | Arweave | Long-term memory / reference library | Long-lived, versioned | Shared (agent world model) |
| **Knowledge Graph** | Arweave | Mental model / concept map | Long-lived, evolves | Shared (agent world model) |

---

## Memory

Memories are atomic units of learned state. They represent things the agent has observed, inferred, or been told.

### Memory Tiers

| Tier | Scope | Storage | Encryption | Example |
|------|-------|---------|------------|---------|
| `user` | Per-user | IPFS | AES-256-GCM (wallet-derived key) | "User prefers concise responses" |
| `agent` | Per-agent | Arweave | None (public) | "Web search returns better results with quoted phrases" |
| `global` | All agents | Arweave | None (public) | "The US Fed meets 8 times per year" |

**User memories are encrypted client-side and stored on IPFS.** Only the wallet holder can decrypt them. Agent and global memories are public, stored on Arweave as part of the shared world model.

### Memory Types

| Type | Description |
|------|-------------|
| `observation` | Direct observation from conversation - "User mentioned they work at a startup" |
| `inference` | Derived conclusion - "User likely interested in fundraising given startup context" |
| `preference` | Expressed or inferred preference - "User prefers data-backed responses" |
| `fact` | Stated fact - "Bitcoin's max supply is 21 million" |
| `episode` | Summary of a significant interaction - "Helped user debug a Python async issue" |

### Memory Schema

```json
{
  "id": "mem_<uuid>",
  "tier": "global|user|agent",
  "wallet_address": null,
  "agent_id": null,
  "type": "observation|inference|preference|fact|episode",
  "content": "User prefers concise responses with data backing",
  "tags": ["preference", "communication"],
  "embedding": [],
  "created_at": "2026-03-02T10:00:00Z",
  "last_accessed": "2026-03-02T10:00:00Z",
  "age": 0,
  "relevance_score": 0.95,
  "accuracy_score": 1.0,
  "impact_score": 0.7,
  "superseded_by": null,
  "source_thread": "thread_abc",
  "metadata": {}
}
```

Note: For user-tier memories, the entire entry (including embedding) is encrypted before storage. The schema above shows the decrypted structure.

### Memory Operations

| Operation | User-tier | Shared-tier |
|-----------|-----------|-------------|
| `store(memory, encryption_key?)` | Encrypt → store on IPFS | Store on Arweave |
| `recall(query, decryption_key?)` | Fetch from IPFS → decrypt → score | Fetch from Arweave → score |
| `query(filters, decryption_key?)` | Fetch → decrypt → filter | Filter directly |
| `update(id, encryption_key?)` | Decrypt → update → re-encrypt → store | Append new version on Arweave |
| `prune(threshold, decryption_key?)` | Requires key (active session only) | Runs independently |
| `consolidate(ids, encryption_key?)` | Requires key (active session only) | Runs independently |
| `supersede(old, new)` | Mark superseded | Mark superseded |

### Scoring Formula

Each memory gets a composite score for retrieval ranking:

```
score = (w_r * relevance) + (w_a * accuracy) + (w_i * impact) - (w_d * decay(age))
```

Where:
- `relevance` - Cosine similarity between query embedding and memory embedding
- `accuracy` - Confidence in the memory's correctness (starts at 1.0, can be downgraded)
- `impact` - How important this memory is (preferences and key facts score higher)
- `decay(age)` - Time-based decay function (memories fade unless reinforced)

Default weights: `w_r=0.4, w_a=0.25, w_i=0.2, w_d=0.15`

---

## Knowledge Base

The knowledge base stores long-lived, structured knowledge as Markdown files with typed YAML frontmatter. This is the agents' shared world model - stored on Arweave, permanent and public. It contains no user-specific information.

### KB Entity Types

| Type | Description | Example |
|------|-------------|---------|
| `entity` | A thing in the world | Bitcoin, a company, a person |
| `fact` | A verified, structured fact | "BTC max supply is 21M" |
| `model` | A logical model or framework | "Porter's Five Forces applied to crypto" |
| `script` | An agent-written script or procedure | "How to analyze a DeFi protocol" |

### KB Entity Schema (Markdown + YAML frontmatter)

```yaml
---
id: kb_<uuid>
type: entity|fact|model|script
tags: [crypto, bitcoin]
created_at: 2026-03-02T10:00:00Z
updated_at: 2026-03-02T10:00:00Z
embedding: []
numerical_facts:
  btc_max_supply: 21000000
superseded_by: null
valid_until: null
---
# Bitcoin

Bitcoin is a decentralized cryptocurrency created in 2009 by Satoshi Nakamoto.
```

### KB Operations

| Operation | Description |
|-----------|-------------|
| `read(id)` | Load a KB entity from Arweave by ID |
| `write(entity)` | Store/update KB entity on Arweave (append-only - new transaction) |
| `search(query)` | Semantic search using public embeddings (Voyage AI) |
| `list(type, tags)` | List entities matching filters |
| `delete(id)` | Mark as deleted on Arweave (append-only) |
| `reindex()` | Rebuild all embeddings using Voyage AI |

---

## Knowledge Graph

The knowledge graph captures relationships between concepts. Stored on Arweave as part of the shared world model - permanent, public, no user-specific data.

### Node and Edge Types

**Nodes:** concept, entity, asset, person, stock, file, event

**Edges:** conceptual, impacts, owns, related_to, causes

### Graph Operations

| Operation | Description |
|-----------|-------------|
| `add_node(node)` | Create a node on Arweave, generate embedding (Voyage AI) |
| `add_edge(edge)` | Create an edge between two nodes |
| `get_node(id)` | Retrieve a node from Arweave |
| `get_neighbors(id, type, depth)` | Traverse graph from a node |
| `query(query, type)` | Semantic search over nodes |
| `shortest_path(source, target)` | Find shortest path between nodes |
| `prune()` | Remove expired nodes and edges |

---

## Dual Embedding Model

| Scope | Model | Where it runs | Privacy |
|-------|-------|---------------|---------|
| Private (user data) | sentence-transformers (all-MiniLM-L6-v2) | Locally on the server | User data never leaves the server |
| Public (shared cognition) | Voyage AI (voyage-3-lite) | External API | Data is public anyway |

User data embeddings are stored encrypted alongside the data - they never touch external APIs.

---

## Temporal Model

All cognitive components have temporal awareness:

- **Memories** have `created_at`, `last_accessed`, and `age` - they decay over time unless reinforced by access
- **KB entities** have `created_at`, `updated_at`, and optional `valid_until` - they can expire
- **Graph nodes and edges** have `created_at` and optional `valid_until` - relationships can expire

---

## Sleep Phase (Maintenance)

The sleep phase runs in two modes:

### Shared cognition maintenance (runs independently)
1. Re-index KB embeddings (Voyage AI)
2. Prune expired graph nodes and edges
3. Strengthen reinforced graph edges

### User-tier maintenance (active sessions only - requires decryption key)
1. Recalculate composite scores with updated decay
2. Prune memories below threshold
3. Consolidate similar memories into stronger entries

User-tier maintenance only runs when the user's decryption key is available (during active sessions). The platform cannot perform maintenance on encrypted data without the key.
