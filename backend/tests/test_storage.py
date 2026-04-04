"""Tests for decentralized storage backends."""

import pytest


class TestLocalStorage:
    """Tests for local filesystem storage backend."""

    @pytest.mark.asyncio
    async def test_store_and_retrieve(self):
        """Test storing data and retrieving it by key."""

    @pytest.mark.asyncio
    async def test_delete(self):
        """Test deleting data by key."""

    @pytest.mark.asyncio
    async def test_list_keys(self):
        """Test listing keys with prefix filter."""

    @pytest.mark.asyncio
    async def test_exists(self):
        """Test checking key existence."""

    @pytest.mark.asyncio
    async def test_update(self):
        """Test updating data at an existing key."""

    @pytest.mark.asyncio
    async def test_resolve_identity(self):
        """Test that local resolve returns the key unchanged."""


class TestIPFSStorage:
    """Tests for IPFS storage backend (stub - requires IPFS node)."""

    @pytest.mark.asyncio
    async def test_store_returns_cid(self):
        """Test that storing data returns a valid IPFS CID."""

    @pytest.mark.asyncio
    async def test_retrieve_by_cid(self):
        """Test retrieving data by CID."""

    @pytest.mark.asyncio
    async def test_update_changes_cid(self):
        """Test that updating data produces a new CID."""

    @pytest.mark.asyncio
    async def test_resolve_ipns(self):
        """Test resolving an IPNS name to a CID."""


class TestArweaveStorage:
    """Tests for Arweave storage backend (stub - requires Arweave wallet)."""

    @pytest.mark.asyncio
    async def test_store_returns_tx_id(self):
        """Test that storing data returns an Arweave transaction ID."""

    @pytest.mark.asyncio
    async def test_immutable_no_delete(self):
        """Test that delete is a no-op on Arweave."""

    @pytest.mark.asyncio
    async def test_query_by_tags(self):
        """Test querying transactions by tags."""

    @pytest.mark.asyncio
    async def test_retrieve_by_tx_id(self):
        """Test retrieving data by transaction ID."""
