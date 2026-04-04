"""AES-256-GCM encryption for user-scoped data.

All user data (memories, preferences, threads) is encrypted client-side before
reaching the server. The platform never sees plaintext user data.

Encryption flow:
1. User signs a deterministic message with their wallet
2. Key is derived from the signature via HKDF-SHA256 (see keys.py)
3. Data is encrypted with AES-256-GCM using a random nonce
4. Encrypted payload (nonce + ciphertext + tag) is stored on IPFS/local

Decryption is the reverse - only the wallet holder can derive the key.
"""

from dataclasses import dataclass


@dataclass
class EncryptedPayload:
    """Container for AES-256-GCM encrypted data.

    Attributes:
        nonce: 12-byte random nonce (IV) used for this encryption.
        ciphertext: The encrypted data bytes.
        tag: 16-byte GCM authentication tag for tamper detection.
    """

    nonce: bytes
    ciphertext: bytes
    tag: bytes


def encrypt(plaintext: bytes, key: bytes) -> EncryptedPayload:
    """Encrypt data with AES-256-GCM.

    Args:
        plaintext: The data to encrypt.
        key: 32-byte AES-256 key (derived from wallet signature).

    Returns:
        EncryptedPayload with nonce, ciphertext, and authentication tag.
    """
    raise NotImplementedError


def decrypt(payload: EncryptedPayload, key: bytes) -> bytes:
    """Decrypt an AES-256-GCM encrypted payload.

    Args:
        payload: The encrypted payload (nonce + ciphertext + tag).
        key: 32-byte AES-256 key (same key used for encryption).

    Returns:
        The decrypted plaintext bytes.

    Raises:
        ValueError: If the authentication tag is invalid (data was tampered with).
    """
    raise NotImplementedError


def serialize_payload(payload: EncryptedPayload) -> bytes:
    """Serialize an EncryptedPayload to bytes for storage.

    Format: nonce (12 bytes) || tag (16 bytes) || ciphertext (variable)

    Args:
        payload: The encrypted payload to serialize.

    Returns:
        Concatenated bytes suitable for storage.
    """
    raise NotImplementedError


def deserialize_payload(data: bytes) -> EncryptedPayload:
    """Deserialize bytes back into an EncryptedPayload.

    Args:
        data: Serialized payload bytes (from serialize_payload).

    Returns:
        The reconstructed EncryptedPayload.

    Raises:
        ValueError: If the data is too short or malformed.
    """
    raise NotImplementedError
