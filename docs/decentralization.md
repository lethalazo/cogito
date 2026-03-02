# Decentralization

Cogito is trustless and decentralized from the MVP. Users don't need to trust the platform with their data, their identity, or their privacy.

## Authentication: SIWE (Sign-In with Ethereum)

No passwords, no emails, no centralized identity provider. Your wallet is your identity.

### Flow

```
1. Client → GET /auth/nonce
   ← { nonce: "abc123" }

2. Client constructs SIWE message:
   "cogito.ai wants you to sign in with your Ethereum account:
   0xABC...123
   Sign in to Cogito
   Nonce: abc123
   Issued At: 2026-03-02T10:00:00Z"

3. User signs message with wallet (MetaMask, WalletConnect, etc.)

4. Client → POST /auth/verify
   { message: "...", signature: "0x..." }
   ← { token: "jwt...", wallet_address: "0xABC...123" }

5. Client includes JWT in all subsequent requests:
   Authorization: Bearer jwt...
```

### Why SIWE?

- **Trustless** — No centralized auth server to trust or compromise
- **Portable** — Your identity works across any Cogito instance
- **Anonymous** — No PII required, just a wallet address
- **Standard** — EIP-4361, widely supported by wallets and dApps

## Storage: IPFS + Arweave

Two storage backends for two data scopes:

### User Data → IPFS (Mutable, Encrypted)

User-scoped data (memories, preferences, threads) is stored on IPFS:
- **Encrypted** — AES-256-GCM with wallet-derived key, before reaching the server
- **Mutable** — IPNS provides mutable pointers for updates
- **Pinned** — Data persists as long as it's pinned (by the user or a pinning service)
- **Portable** — Users can migrate to any IPFS-compatible node

```
User data flow:
  plaintext → [encrypt with wallet-derived key] → ciphertext → [store on IPFS] → CID
  CID → [fetch from IPFS] → ciphertext → [decrypt with wallet-derived key] → plaintext
```

### Shared Cognition → Arweave (Permanent, Public)

The agent's world model (KB, graph) is stored on Arweave:
- **Permanent** — Data is stored forever, pay once
- **Public** — No encryption, this is world knowledge (no user-specific data)
- **Immutable** — Append-only, updates create new transactions
- **Queryable** — Tagged data, queryable via GraphQL
- **Permissionless** — Anyone can read the agent's world model

```
Shared cognition flow:
  world knowledge → [tag with metadata] → [store on Arweave] → transaction ID
  transaction ID → [fetch from Arweave] → world knowledge
```

### Local Storage (Dev / Self-Hosted)

For development and self-hosted deployments, a local filesystem backend is available:
- Same interface as IPFS/Arweave
- Data stored as files under a configurable directory
- Encryption still applies for user data

## Encryption: Wallet-Derived Keys + Lit Protocol

### Wallet-Derived Keys

Users derive their encryption key from their wallet:

```
1. Client requests deterministic message to sign
2. User signs with wallet → signature
3. HKDF-SHA256(signature) → 32-byte AES-256 key
4. Key encrypts/decrypts all user data
```

The key never leaves the client. The server never sees the signature. Only the wallet holder can derive the key.

### Lit Protocol (Decentralized Key Management)

For advanced access control (e.g., sharing encrypted data between wallets), Lit Protocol provides:
- **Decentralized encryption** — No centralized key custodian
- **Access control conditions** — On-chain conditions that must be met to decrypt
- **Threshold cryptography** — No single Lit node has the full key
- **Programmable** — Conditions can check wallet ownership, token balances, NFTs, etc.

## Self-Hosted Nodes

Users can run their own Cogito instance:
- **Read shared cognition from Arweave** — Read-only access to the agent's world model
- **Store user data locally** — No IPFS dependency required
- **Maintain private internal cognition** — Self-hosted nodes can build on top of shared cognition
- **Bring your own LLM** — Self-hosted nodes can use any LLM (Claude, local models, etc.)
- **Pay via USDC** — Pay-as-you-go for compute on Payproof rails

```
Self-hosted architecture:
  [User's Node]
      ├── Local user data (encrypted)
      ├── Read-only Arweave (shared cognition)
      ├── LLM API (Claude / local)
      └── USDC payments (Payproof)
```

## Threat Model

| Threat | Mitigation |
|--------|-----------|
| Platform reads user data | Client-side encryption — platform never sees plaintext |
| Platform loses user data | IPFS replication + user can re-pin from any node |
| Platform goes offline | Self-hosted nodes read from Arweave (permissionless) |
| Key compromise | Wallet-derived keys — rotate by signing with a new wallet |
| Man-in-the-middle | HTTPS + SIWE nonces prevent replay attacks |
| Platform censors users | Arweave data is permanent and censorship-resistant |
