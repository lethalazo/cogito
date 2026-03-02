"""FastAPI application and route definitions."""

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="Cogito",
    description="Cognitive AI agent framework API",
    version="0.1.0",
)


class ChatRequest(BaseModel):
    message: str
    thread_id: str | None = None
    user_id: str = "default"


class ChatResponse(BaseModel):
    response: str
    thread_id: str


class MemoryRequest(BaseModel):
    content: str
    tier: str = "global"
    memory_type: str = "observation"
    tags: list[str] = []


@app.get("/health")
async def health():
    """Health check endpoint."""
    return {"status": "ok"}


@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """Send a message and get a response from the agent.

    Creates a new thread if thread_id is not provided.
    """
    raise NotImplementedError


@app.get("/threads")
async def list_threads(user_id: str = "default"):
    """List all conversation threads for a user."""
    raise NotImplementedError


@app.get("/threads/{thread_id}")
async def get_thread(thread_id: str):
    """Get a thread's message history."""
    raise NotImplementedError


@app.get("/memory")
async def query_memory(
    q: str | None = None,
    tier: str | None = None,
    memory_type: str | None = None,
    limit: int = 20,
):
    """Query memories by semantic search or structured filters."""
    raise NotImplementedError


@app.post("/memory")
async def store_memory(request: MemoryRequest):
    """Manually store a new memory."""
    raise NotImplementedError
