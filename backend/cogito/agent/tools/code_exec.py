"""Code execution tool - execute Python code in a sandbox."""

from typing import Any

TOOL_DEFINITION: dict[str, Any] = {
    "name": "code_exec",
    "description": "Execute Python code in a sandboxed environment and return the output.",
    "input_schema": {
        "type": "object",
        "properties": {
            "code": {
                "type": "string",
                "description": "The Python code to execute.",
            },
        },
        "required": ["code"],
    },
}


async def execute(code: str) -> str:
    """Execute Python code in a sandbox.

    Args:
        code: The Python code to run.

    Returns:
        The stdout output of the code execution.
    """
    raise NotImplementedError
