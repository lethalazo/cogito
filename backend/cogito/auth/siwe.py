"""SIWE (Sign-In with Ethereum) — trustless wallet-based authentication.

Authentication flow:
1. Client requests a nonce from GET /auth/nonce
2. Client constructs a SIWE message with the nonce, domain, and wallet address
3. User signs the message with their wallet (MetaMask, WalletConnect, etc.)
4. Client sends the message + signature to POST /auth/verify
5. Server verifies the signature matches the wallet address in the message
6. Server creates a JWT session token and returns it
7. Client includes the JWT in subsequent requests via Authorization header

No passwords, no emails, no centralized identity provider. Your wallet is your identity.
"""

from dataclasses import dataclass
from datetime import datetime


@dataclass
class SIWEMessage:
    """A Sign-In with Ethereum message.

    Attributes:
        domain: The domain requesting the sign-in (e.g., "cogito.ai").
        address: The Ethereum wallet address (checksummed).
        statement: Human-readable statement of intent.
        uri: The URI the user is signing in to.
        version: SIWE message version (always "1").
        chain_id: The Ethereum chain ID (1 for mainnet).
        nonce: Random nonce to prevent replay attacks.
        issued_at: When the message was created.
        expiration_time: When the message expires (optional).
    """

    domain: str
    address: str
    statement: str
    uri: str
    version: str = "1"
    chain_id: int = 1
    nonce: str = ""
    issued_at: datetime | None = None
    expiration_time: datetime | None = None


def generate_nonce() -> str:
    """Generate a cryptographically random nonce for SIWE.

    Returns:
        A random alphanumeric nonce string.
    """
    raise NotImplementedError


def create_message(
    domain: str,
    address: str,
    nonce: str,
    statement: str = "Sign in to Cogito",
    chain_id: int = 1,
) -> SIWEMessage:
    """Create a SIWE message for the user to sign.

    Args:
        domain: The domain requesting sign-in.
        address: The user's Ethereum wallet address.
        nonce: The nonce from generate_nonce().
        statement: Human-readable statement of intent.
        chain_id: Ethereum chain ID.

    Returns:
        A SIWEMessage ready for the user to sign.
    """
    raise NotImplementedError


def verify_signature(message: SIWEMessage, signature: str) -> bool:
    """Verify that a SIWE message was signed by the claimed wallet address.

    Args:
        message: The SIWE message that was signed.
        signature: The wallet's signature (hex-encoded).

    Returns:
        True if the signature is valid and matches the address in the message.
    """
    raise NotImplementedError
