"""Tests for the memory store."""

import pytest


class TestMemoryStore:
    """Tests for MemoryStore CRUD operations."""

    @pytest.mark.asyncio
    async def test_store_and_recall(self):
        """Test storing a memory and recalling it by semantic query."""

    @pytest.mark.asyncio
    async def test_store_with_tiers(self):
        """Test that memories respect tier scoping (global, user, agent)."""

    @pytest.mark.asyncio
    async def test_query_by_type(self):
        """Test filtering memories by type."""

    @pytest.mark.asyncio
    async def test_prune_below_threshold(self):
        """Test that pruning removes low-score memories."""

    @pytest.mark.asyncio
    async def test_consolidate_similar(self):
        """Test merging similar memories into a single entry."""

    @pytest.mark.asyncio
    async def test_supersede(self):
        """Test marking a memory as superseded by a newer version."""
