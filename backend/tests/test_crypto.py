"""Tests for encryption and key management."""

import pytest


class TestEncryption:
    """Tests for AES-256-GCM encryption/decryption."""

    @pytest.mark.asyncio
    async def test_encrypt_decrypt_roundtrip(self):
        """Test that encrypt → decrypt returns the original plaintext."""

    @pytest.mark.asyncio
    async def test_different_nonce_per_encryption(self):
        """Test that each encryption produces a unique nonce."""

    @pytest.mark.asyncio
    async def test_tamper_detection(self):
        """Test that modified ciphertext is detected via GCM auth tag."""

    @pytest.mark.asyncio
    async def test_wrong_key_fails(self):
        """Test that decryption with wrong key raises ValueError."""

    @pytest.mark.asyncio
    async def test_serialize_deserialize_payload(self):
        """Test roundtrip serialization of EncryptedPayload."""


class TestKeyDerivation:
    """Tests for wallet-derived key management."""

    @pytest.mark.asyncio
    async def test_derive_key_deterministic(self):
        """Test that same signature produces same derived key."""

    @pytest.mark.asyncio
    async def test_derive_key_length(self):
        """Test that derived key is 32 bytes (AES-256)."""

    @pytest.mark.asyncio
    async def test_different_wallets_different_keys(self):
        """Test that different wallet signatures produce different keys."""

    @pytest.mark.asyncio
    async def test_key_derivation_message_deterministic(self):
        """Test that the message to sign is deterministic for a given wallet."""
