# Privacy Model

Cogito separates data into two scopes with fundamentally different privacy properties. User data is always encrypted. Shared cognition is always public. The boundary is strict and enforced by architecture, not policy.

## Two Data Scopes

| Scope | What | Storage | Encryption | Embeddings | Access |
|-------|------|---------|------------|------------|--------|
| **User-scoped** | Memories, preferences, threads, profile | IPFS (mutable, pinned) | AES-256-GCM, wallet-derived key | Local model (sentence-transformers) | Only wallet holder |
| **Shared cognition** | KB entities, graph nodes/edges, world model | Arweave (permanent, immutable) | None (public) | Voyage AI | Anyone (permissionless) |

## User-Scoped Data

### What's in this scope
- **Memories**: Observations, inferences, preferences, facts, episodes about/from the user
- **Threads**: Conversation history
- **Profile**: User settings and preferences

### Privacy guarantees
- **Encrypted client-side** — Data is encrypted before reaching the server using AES-256-GCM
- **Wallet-derived key** — Encryption key is derived from a wallet signature via HKDF-SHA256
- **Platform-blind** — The server never sees plaintext user data
- **Private embeddings** — User data is embedded using a local model (sentence-transformers), never sent to external APIs
- **Per-user isolation** — Each wallet's data is cryptographically separated

### Session data flow

```
During an active session:
  1. Fetch encrypted user data from IPFS
  2. Decrypt client-side with wallet-derived key
  3. Agent processes decrypted data in-memory
  4. New learnings encrypted with wallet-derived key
  5. Store encrypted data back to IPFS
  6. Plaintext only exists in-memory during the session
```

## Shared Cognition

### What's in this scope
- **Knowledge base**: Entities, facts, models, scripts — world knowledge
- **Knowledge graph**: Concepts, relationships, causality — relational world model
- **Agent state**: Agent-tier memories — things the agent has learned about how to be effective

### Privacy guarantees
- **No user data ever enters shared cognition** — This is enforced at the architecture level
- **Public and permanent** — Stored on Arweave, readable by anyone
- **Public embeddings** — Embedded using Voyage AI (the data is public anyway)

### What never goes into shared cognition
- User names, wallet addresses, or any PII
- User preferences or personal opinions
- User conversation content
- Any data that could identify or profile a specific user

## Embeddings Problem

Embeddings are a privacy concern because they can partially reconstruct the source text. Cogito solves this with dual embedding models:

| Data Type | Embedding Model | Privacy |
|-----------|----------------|---------|
| User memories, preferences | sentence-transformers (all-MiniLM-L6-v2) | Runs locally, no data leaves the server |
| KB entities, graph nodes | Voyage AI (voyage-3-lite) | Data is public anyway |

User data embeddings are stored encrypted alongside the data — they never touch external APIs.

## Encryption Details

### Algorithm: AES-256-GCM
- **Key size**: 256 bits (32 bytes)
- **Nonce**: 12 bytes, randomly generated per encryption
- **Authentication**: GCM provides authenticated encryption (tamper detection)
- **Payload**: nonce (12B) || tag (16B) || ciphertext (variable)

### Key Derivation: HKDF-SHA256
- **Input**: Wallet signature of a deterministic message
- **Output**: 32-byte AES-256 key
- **Deterministic**: Same wallet + same message = same key (reproducible across sessions)
- **Wallet-bound**: Only the wallet holder can produce the source signature

### Lit Protocol (Advanced)
- Decentralized key management for access control conditions
- Threshold cryptography — no single node has the full key
- Supports wallet ownership checks, token gating, and programmable conditions

## Threat Model

| Threat | Impact | Mitigation |
|--------|--------|-----------|
| Server compromise | Attacker gets encrypted blobs | Useless without wallet-derived keys |
| Embedding inversion | Partial text reconstruction from embeddings | User embeddings are encrypted and use local model |
| Cross-user data leakage | User A sees User B's data | Per-wallet encryption keys, separate IPFS storage |
| LLM context leakage | LLM memorizes user data | Per-session context, no fine-tuning on user data |
| Malicious agent update | Agent code exfiltrates data | Agent code is open-source, auditable |
| Key loss | User loses access to data | Wallet recovery = key recovery (same derivation) |
