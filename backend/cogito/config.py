"""Application configuration and settings."""

from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class Settings:
    """Global application settings."""

    # API keys
    anthropic_api_key: str = ""
    voyage_api_key: str = ""

    # Paths
    data_dir: Path = Path("data")
    agents_dir: Path = Path("agents")

    # Model defaults
    default_model: str = "claude-sonnet-4-20250514"
    default_max_tokens: int = 8192
    embedding_model: str = "voyage-3-lite"

    # Cognition
    memory_score_threshold: float = 0.3
    memory_decay_rate: float = 0.01
    max_recall_results: int = 20

    # Scoring weights
    relevance_weight: float = 0.4
    accuracy_weight: float = 0.25
    impact_weight: float = 0.2
    decay_weight: float = 0.15

    @property
    def memory_dir(self) -> Path:
        return self.data_dir / "memory"

    @property
    def kb_dir(self) -> Path:
        return self.data_dir / "knowledge_base"

    @property
    def graph_dir(self) -> Path:
        return self.data_dir / "graph"

    @property
    def users_dir(self) -> Path:
        return self.data_dir / "users"


def load_settings() -> Settings:
    """Load settings from environment variables and config files."""
    raise NotImplementedError
