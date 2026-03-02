"""Wallet-derived key management — deterministic key derivation from wallet signatures.

Key derivation flow:
1. Client requests a deterministic message to sign (key_derivation_message)
2. User signs the message with their wallet (MetaMask, WalletConnect, etc.)
3. The signature is passed to derive_key_from_signature
4. HKDF-SHA256 derives a 32-byte AES-256 key from the signature
5. This key encrypts/decrypts all user-scoped data

The key never leaves the client. The server never sees the signature or the derived key.
Only the wallet holder can produce the signature, so only they can derive the key.
"""

from dataclasses import dataclass


@dataclass
class DerivedKey:
    """A key derived from a wallet signature.

    Attributes:
        key: 32-byte AES-256 key for encryption/decryption.
        wallet_address: The wallet address that produced the source signature.
        salt: The salt used in HKDF derivation (for reproducibility).
    """

    key: bytes
    wallet_address: str
    salt: bytes


def key_derivation_message(wallet_address: str) -> str:
    """Generate the deterministic message for the user to sign.

    This message is always the same for a given wallet address, ensuring
    the derived key is reproducible across sessions.

    Args:
        wallet_address: The user's Ethereum wallet address (checksummed).

    Returns:
        The message string for the user to sign.
    """
    raise NotImplementedError


def derive_key_from_signature(signature: bytes, wallet_address: str) -> DerivedKey:
    """Derive an AES-256 encryption key from a wallet signature using HKDF-SHA256.

    Args:
        signature: The wallet's signature of the key derivation message.
        wallet_address: The wallet address that produced the signature.

    Returns:
        A DerivedKey containing the 32-byte AES-256 key.
    """
    raise NotImplementedError
