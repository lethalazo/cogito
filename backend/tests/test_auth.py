"""Tests for wallet authentication - SIWE and session management."""

import pytest


class TestSIWE:
    """Tests for Sign-In with Ethereum message creation and verification."""

    @pytest.mark.asyncio
    async def test_create_message(self):
        """Test creating a valid SIWE message."""

    @pytest.mark.asyncio
    async def test_verify_valid_signature(self):
        """Test verifying a correctly signed SIWE message."""

    @pytest.mark.asyncio
    async def test_verify_invalid_signature(self):
        """Test that an invalid signature is rejected."""

    @pytest.mark.asyncio
    async def test_generate_nonce_unique(self):
        """Test that generated nonces are unique."""

    @pytest.mark.asyncio
    async def test_expired_message_rejected(self):
        """Test that expired SIWE messages are rejected."""


class TestSession:
    """Tests for JWT session management."""

    @pytest.mark.asyncio
    async def test_create_session(self):
        """Test creating a JWT session from a wallet address."""

    @pytest.mark.asyncio
    async def test_verify_valid_session(self):
        """Test verifying a valid JWT session token."""

    @pytest.mark.asyncio
    async def test_verify_expired_session(self):
        """Test that expired JWT tokens are rejected."""

    @pytest.mark.asyncio
    async def test_revoke_session(self):
        """Test that revoked sessions cannot be used."""

    @pytest.mark.asyncio
    async def test_session_contains_wallet_address(self):
        """Test that the session contains the correct wallet address."""
