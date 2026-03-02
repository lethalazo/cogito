"""Wallet authentication — SIWE (Sign-In with Ethereum) and session management."""

from cogito.auth.middleware import get_current_session, wallet_address_from_session
from cogito.auth.session import Session, create_session, revoke_session, verify_session
from cogito.auth.siwe import SIWEMessage, create_message, generate_nonce, verify_signature

__all__ = [
    "SIWEMessage",
    "create_message",
    "verify_signature",
    "generate_nonce",
    "Session",
    "create_session",
    "verify_session",
    "revoke_session",
    "get_current_session",
    "wallet_address_from_session",
]
