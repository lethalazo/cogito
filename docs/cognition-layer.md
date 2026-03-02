# Cognition Layer

The cognition layer is what makes Cogito more than a chatbot. It provides persistent memory, structured knowledge, and relational understanding across conversations.

## Three Cognitive Components

| Component | Storage | Analogy | Lifespan |
|-----------|---------|---------|----------|
| **Memory** | JSONL | Working memory / episodic memory | Short-to-medium term, decays |
| **Knowledge Base** | Markdown + YAML | Long-term memory / reference library | Long-lived, versioned |
| **Knowledge Graph** | JSONL (nodes + edges) | Mental model / concept map | Long-lived, evolves |

---

## Memory

Memories are atomic units of learned state. They represent things the agent has observed, inferred, or been told.

### Memory Tiers

| Tier | Scope | Example |
|------|-------|---------|
| `global` | Shared across all users and agents | "The US Fed meets 8 times per year" |
| `user` | Scoped to a specific user | "Arsalan prefers concise responses" |
| `agent` | Scoped to a specific agent's learned state | "Web search tool returns better results with quoted phrases" |

### Memory Types

| Type | Description |
|------|-------------|
| `observation` | Direct observation from conversation — "User mentioned they work at a startup" |
| `inference` | Derived conclusion — "User likely interested in fundraising given startup context" |
| `preference` | Expressed or inferred preference — "User prefers data-backed responses" |
| `fact` | Stated fact — "Bitcoin's max supply is 21 million" |
| `episode` | Summary of a significant interaction — "Helped user debug a Python async issue" |

### Memory Schema (JSONL)

```json
{
  "id": "mem_<uuid>",
  "tier": "global|user|agent",
  "user_id": null,
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

### Memory Operations

| Operation | Description |
|-----------|-------------|
| `store(memory)` | Create a new memory entry, generate embedding |
| `recall(query, tier, limit)` | Semantic search + scoring to find relevant memories |
| `query(filters)` | Filter memories by tier, type, tags, date range |
| `update(id, fields)` | Update specific fields (e.g., accuracy score) |
| `prune(threshold)` | Remove memories below score threshold |
| `consolidate(ids)` | Merge similar memories into a single stronger entry |
| `supersede(old_id, new_id)` | Mark a memory as replaced by a newer version |

### Scoring Formula

Each memory gets a composite score for retrieval ranking:

```
score = (w_r * relevance) + (w_a * accuracy) + (w_i * impact) - (w_d * decay(age))
```

Where:
- `relevance` — Cosine similarity between query embedding and memory embedding
- `accuracy` — Confidence in the memory's correctness (starts at 1.0, can be downgraded)
- `impact` — How important this memory is (preferences and key facts score higher)
- `decay(age)` — Time-based decay function (memories fade unless reinforced)

Default weights: `w_r=0.4, w_a=0.25, w_i=0.2, w_d=0.15`

---

## Knowledge Base

The knowledge base stores long-lived, structured knowledge as Markdown files with typed YAML frontmatter. Think of it as the agent's hard drive — things worth writing down properly.

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
It operates on a proof-of-work blockchain with a fixed maximum supply of 21 million coins.

## Key Properties
- Decentralized, permissionless network
- Fixed supply (deflationary by design)
- Proof-of-work consensus (SHA-256)
- ~10 minute block time
```

### KB Index Schema (JSONL)

The knowledge base maintains a separate index file for fast search:

```json
{
  "id": "kb_<uuid>",
  "path": "entities/bitcoin.md",
  "type": "entity",
  "title": "Bitcoin",
  "tags": ["crypto", "bitcoin"],
  "embedding": [],
  "updated_at": "2026-03-02T10:00:00Z"
}
```

### KB Operations

| Operation | Description |
|-----------|-------------|
| `read(id)` | Load a KB entity by ID |
| `write(entity)` | Create or update a KB entity, regenerate embedding, update index |
| `search(query, type, tags)` | Semantic search over KB index |
| `list(type, tags)` | List entities matching filters |
| `delete(id)` | Remove entity and its index entry |
| `reindex()` | Rebuild all embeddings and the index file |

---

## Knowledge Graph

The knowledge graph captures relationships between concepts. It enables the agent to reason about connections, trace impact chains, and discover non-obvious relationships.

### Node Types

| Type | Description |
|------|-------------|
| `concept` | Abstract concept — "inflation", "decentralization" |
| `entity` | Concrete entity — "Bitcoin", "Federal Reserve" |
| `asset` | Financial asset — "BTC", "AAPL" |
| `person` | A person — "Satoshi Nakamoto" |
| `stock` | A stock or equity — "NVDA" |
| `file` | A file reference — links to KB entities |
| `event` | An event — "Bitcoin halving 2024" |

### Edge Types

| Type | Description |
|------|-------------|
| `conceptual` | Abstract relationship — "Bitcoin" is a "cryptocurrency" |
| `impacts` | Causal impact — "Fed rate hike" impacts "crypto market" |
| `owns` | Ownership — "User" owns "BTC" |
| `related_to` | General relationship — "Ethereum" related to "smart contracts" |
| `causes` | Direct causation — "halving" causes "supply reduction" |

### Node Schema (JSONL)

```json
{
  "id": "node_<uuid>",
  "type": "concept|entity|asset|person|stock|file|event",
  "label": "Bitcoin",
  "tags": ["crypto"],
  "embedding": [],
  "metadata": {},
  "created_at": "2026-03-02T10:00:00Z",
  "valid_until": null
}
```

### Edge Schema (JSONL)

```json
{
  "id": "edge_<uuid>",
  "source": "node_xxx",
  "target": "node_yyy",
  "type": "conceptual|impacts|owns|related_to|causes",
  "weight": 0.8,
  "label": "Bitcoin impacts crypto market sentiment",
  "tags": [],
  "embedding": [],
  "metadata": {},
  "created_at": "2026-03-02T10:00:00Z",
  "valid_until": null
}
```

### Graph Operations

| Operation | Description |
|-----------|-------------|
| `add_node(node)` | Create a node, generate embedding |
| `add_edge(edge)` | Create an edge between two nodes |
| `get_node(id)` | Retrieve a node by ID |
| `get_neighbors(node_id, edge_type, depth)` | Traverse graph from a node |
| `query(query, node_type)` | Semantic search over nodes |
| `shortest_path(source, target)` | Find shortest path between nodes |
| `prune(valid_until)` | Remove expired nodes and their edges |

---

## Temporal Model

All cognitive components have temporal awareness:

- **Memories** have `created_at`, `last_accessed`, and `age` — they decay over time unless reinforced by access
- **KB entities** have `created_at`, `updated_at`, and optional `valid_until` — they can expire
- **Graph nodes and edges** have `created_at` and optional `valid_until` — relationships can expire

This temporal model enables:
- Automatic decay of stale information
- Prioritization of recent and frequently-accessed knowledge
- Expiration of time-sensitive facts (e.g., "current Bitcoin price")

---

## Sleep Phase (Maintenance)

The sleep phase is a periodic maintenance cycle that keeps the cognition layer healthy. It runs on a schedule or can be triggered manually.

### Sleep Phase Steps

1. **Score all memories** — Recalculate composite scores with updated decay
2. **Prune** — Remove memories below the score threshold
3. **Consolidate** — Find clusters of similar memories, merge into single stronger entries
4. **Update graph** — Strengthen edges that have been reinforced, prune expired nodes
5. **Re-index KB** — Regenerate embeddings for updated entities
6. **Report** — Log what was pruned, consolidated, and updated

### Consolidation Example

Before:
- "User likes Python" (relevance: 0.6)
- "User prefers Python over JavaScript" (relevance: 0.7)
- "User uses Python for all backend work" (relevance: 0.8)

After consolidation:
- "User strongly prefers Python, uses it for all backend work, prefers it over JavaScript" (relevance: 0.9)
