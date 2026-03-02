"""FastAPI authentication middleware — session verification as a dependency.

Usage in routes:
    @app.get("/protected")
    async def protected_route(session: Session = Depends(get_current_session)):
        wallet = session.wallet_address
        ...
"""

from cogito.auth.session import Session


async def get_current_session() -> Session:
    """FastAPI dependency that extracts and verifies the session from the request.

    Reads the JWT from the Authorization header (Bearer token), verifies it,
    and returns the authenticated Session.

    Returns:
        The verified Session for the current request.

    Raises:
        HTTPException(401): If no token is provided or the token is invalid.
        HTTPException(403): If the session has been revoked.
    """
    raise NotImplementedError


def wallet_address_from_session(session: Session) -> str:
    """Extract the wallet address from a verified session.

    Convenience function for routes that only need the wallet address.

    Args:
        session: A verified Session (from get_current_session).

    Returns:
        The checksummed Ethereum wallet address.
    """
    return session.wallet_address
