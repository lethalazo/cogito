"""Application configuration and settings — decentralized, privacy-preserving defaults."""

from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class CryptoSettings:
    """Encryption and key management settings."""

    algorithm: str = "AES-256-GCM"
    key_derivation: str = "HKDF-SHA256"
    key_length: int = 32
    nonce_length: int = 12
    lit_network: str = "cayenne"


@dataclass
class StorageSettings:
    """Decentralized storage backend settings.

    User data (memories, preferences, threads) → IPFS (mutable, encrypted).
    Shared cognition (KB, graph, world model) → Arweave (permanent, public).
    Local backend available for dev and self-hosted deployments.
    """

    user_data_backend: str = "ipfs"
    shared_cognition_backend: str = "arweave"

    # IPFS settings
    ipfs_api_url: str = "/ip4/127.0.0.1/tcp/5001"
    ipfs_pin_service: str = ""

    # Arweave settings
    arweave_gateway_url: str = "https://arweave.net"
    arweave_wallet_path: str = ""

    # Local storage (dev / self-hosted fallback)
    local_storage_dir: Path = field(default_factory=lambda: Path("data"))


@dataclass
class AuthSettings:
    """SIWE authentication and session settings."""

    siwe_domain: str = "cogito.ai"
    siwe_statement: str = "Sign in to Cogito"
    jwt_secret: str = ""
    jwt_algorithm: str = "HS256"
    session_expiry_hours: int = 24


@dataclass
class PaymentSettings:
    """USDC payment settings via Payproof rails."""

    enabled: bool = False
    payproof_api_url: str = ""
    usdc_contract_address: str = ""
    chain_id: int = 1


@dataclass
class EmbeddingSettings:
    """Dual embedding model settings.

    Public (shared cognition) → Voyage AI — high-quality embeddings for the world model.
    Private (user-scoped) → sentence-transformers — local model, no data leaves the server.
    """

    public_model: str = "voyage-3-lite"
    private_model: str = "all-MiniLM-L6-v2"


@dataclass
class Settings:
    """Global application settings — decentralized, privacy-preserving defaults."""

    # API keys
    anthropic_api_key: str = ""
    voyage_api_key: str = ""

    # Paths
    agents_dir: Path = Path("agents")

    # Model defaults
    default_model: str = "claude-sonnet-4-20250514"
    default_max_tokens: int = 8192

    # Cognition
    memory_score_threshold: float = 0.3
    memory_decay_rate: float = 0.01
    max_recall_results: int = 20

    # Scoring weights
    relevance_weight: float = 0.4
    accuracy_weight: float = 0.25
    impact_weight: float = 0.2
    decay_weight: float = 0.15

    # Nested settings
    crypto: CryptoSettings = field(default_factory=CryptoSettings)
    storage: StorageSettings = field(default_factory=StorageSettings)
    auth: AuthSettings = field(default_factory=AuthSettings)
    payments: PaymentSettings = field(default_factory=PaymentSettings)
    embeddings: EmbeddingSettings = field(default_factory=EmbeddingSettings)


def load_settings() -> Settings:
    """Load settings from environment variables and config files."""
    raise NotImplementedError
