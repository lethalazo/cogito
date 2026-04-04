"""Browser tool - navigate to a URL and extract content."""

from typing import Any

TOOL_DEFINITION: dict[str, Any] = {
    "name": "browser",
    "description": "Navigate to a URL and extract the page content as text.",
    "input_schema": {
        "type": "object",
        "properties": {
            "url": {
                "type": "string",
                "description": "The URL to navigate to.",
            },
        },
        "required": ["url"],
    },
}


async def execute(url: str) -> str:
    """Navigate to a URL and extract content.

    Args:
        url: The URL to visit.

    Returns:
        Extracted page content as text.
    """
    raise NotImplementedError
