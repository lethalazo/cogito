"""Web search tool - search the web for information."""

from typing import Any

TOOL_DEFINITION: dict[str, Any] = {
    "name": "web_search",
    "description": "Search the web for current information on a topic.",
    "input_schema": {
        "type": "object",
        "properties": {
            "query": {
                "type": "string",
                "description": "The search query.",
            },
        },
        "required": ["query"],
    },
}


async def execute(query: str) -> str:
    """Execute a web search and return results.

    Args:
        query: The search query string.

    Returns:
        Formatted search results.
    """
    raise NotImplementedError
