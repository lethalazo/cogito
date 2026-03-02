"""Session management — JWT-based sessions backed by wallet authentication.

After SIWE verification, a JWT session token is created. The token contains the
wallet address and expiration time. Sessions can be revoked server-side.

Session lifecycle:
1. User authenticates via SIWE → create_session() → JWT token
2. Client includes JWT in Authorization header for all requests
3. Server verifies JWT on each request → verify_session()
4. User logs out → revoke_session() → token is invalidated
"""

from dataclasses import dataclass
from datetime import datetime


@dataclass
class Session:
    """An authenticated user session.

    Attributes:
        wallet_address: The authenticated wallet address (checksummed).
        token: The JWT session token.
        created_at: When the session was created.
        expires_at: When the session expires.
        revoked: Whether the session has been revoked.
    """

    wallet_address: str
    token: str
    created_at: datetime | None = None
    expires_at: datetime | None = None
    revoked: bool = False


def create_session(wallet_address: str) -> Session:
    """Create a new JWT session after successful SIWE authentication.

    Args:
        wallet_address: The verified wallet address.

    Returns:
        A Session with a signed JWT token.
    """
    raise NotImplementedError


def verify_session(token: str) -> Session:
    """Verify a JWT session token and return the session.

    Args:
        token: The JWT token from the Authorization header.

    Returns:
        The verified Session.

    Raises:
        ValueError: If the token is invalid, expired, or revoked.
    """
    raise NotImplementedError


def revoke_session(token: str) -> None:
    """Revoke a session token, preventing further use.

    Args:
        token: The JWT token to revoke.
    """
    raise NotImplementedError
