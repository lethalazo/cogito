"""Tests for the knowledge base store - with decentralized storage backend."""

import pytest


class TestKBStore:
    """Tests for KBStore CRUD operations with StorageBackend."""

    @pytest.mark.asyncio
    async def test_write_and_read(self):
        """Test creating a KB entity and reading it back from storage."""

    @pytest.mark.asyncio
    async def test_search_by_query(self):
        """Test semantic search over KB entities."""

    @pytest.mark.asyncio
    async def test_list_by_type(self):
        """Test listing entities filtered by type."""

    @pytest.mark.asyncio
    async def test_delete(self):
        """Test deleting an entity and its index entry."""

    @pytest.mark.asyncio
    async def test_reindex(self):
        """Test rebuilding the full KB index with public embeddings."""

    @pytest.mark.asyncio
    async def test_no_user_data_in_kb(self):
        """Test that KB operations never store user-specific data."""
