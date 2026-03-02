"""Encryption and key management — client-side encryption for user data privacy."""

from cogito.crypto.encryption import (
    EncryptedPayload,
    decrypt,
    deserialize_payload,
    encrypt,
    serialize_payload,
)
from cogito.crypto.keys import DerivedKey, derive_key_from_signature, key_derivation_message

__all__ = [
    "EncryptedPayload",
    "encrypt",
    "decrypt",
    "serialize_payload",
    "deserialize_payload",
    "DerivedKey",
    "derive_key_from_signature",
    "key_derivation_message",
]
