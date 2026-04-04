"""FastAPI application and route definitions - wallet-authenticated, privacy-preserving API."""

from fastapi import Depends, FastAPI
from pydantic import BaseModel

from cogito.auth.middleware import get_current_session
from cogito.auth.session import Session

app = FastAPI(
    title="Cogito",
    description="Decentralized cognitive AI agent framework API - trustless, privacy-preserving",
    version="0.1.0",
)


# --- Pydantic models ---


class NonceResponse(BaseModel):
    """Response for GET /auth/nonce."""

    nonce: str


class SIWEAuthRequest(BaseModel):
    """Request for POST /auth/verify - SIWE message + wallet signature."""

    message: str
    signature: str


class AuthResponse(BaseModel):
    """Response for POST /auth/verify - JWT session token."""

    token: str
    wallet_address: str


class ChatRequest(BaseModel):
    """Request for POST /chat - no user_id, identity comes from wallet session."""

    message: str
    thread_id: str | None = None


class ChatResponse(BaseModel):
    response: str
    thread_id: str


class MemoryRequest(BaseModel):
    content: str
    tier: str = "global"
    memory_type: str = "observation"
    tags: list[str] = []


# --- Auth endpoints (public) ---


@app.get("/auth/nonce", response_model=NonceResponse)
async def get_nonce():
    """Generate a nonce for SIWE authentication.

    The client uses this nonce to construct a SIWE message for the user to sign.
    """
    raise NotImplementedError


@app.post("/auth/verify", response_model=AuthResponse)
async def verify_auth(request: SIWEAuthRequest):
    """Verify a SIWE signature and create a session.

    The client sends the SIWE message and wallet signature. If valid,
    a JWT session token is returned for subsequent authenticated requests.
    """
    raise NotImplementedError


@app.post("/auth/logout")
async def logout(session: Session = Depends(get_current_session)):
    """Revoke the current session."""
    raise NotImplementedError


# --- Health (public) ---


@app.get("/health")
async def health():
    """Health check endpoint."""
    return {"status": "ok"}


# --- Protected endpoints (require wallet session) ---


@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest, session: Session = Depends(get_current_session)):
    """Send a message and get a response from the agent.

    Creates a new thread if thread_id is not provided.
    User identity is derived from the authenticated wallet session.
    """
    raise NotImplementedError


@app.get("/threads")
async def list_threads(session: Session = Depends(get_current_session)):
    """List all conversation threads for the authenticated wallet."""
    raise NotImplementedError


@app.get("/threads/{thread_id}")
async def get_thread(thread_id: str, session: Session = Depends(get_current_session)):
    """Get a thread's message history.

    Only accessible by the wallet that owns the thread.
    """
    raise NotImplementedError


@app.get("/memory")
async def query_memory(
    q: str | None = None,
    tier: str | None = None,
    memory_type: str | None = None,
    limit: int = 20,
    session: Session = Depends(get_current_session),
):
    """Query memories by semantic search or structured filters.

    User-tier memories are decrypted in-memory for the response.
    """
    raise NotImplementedError


@app.post("/memory")
async def store_memory(
    request: MemoryRequest,
    session: Session = Depends(get_current_session),
):
    """Manually store a new memory.

    User-tier memories are encrypted before storage.
    """
    raise NotImplementedError
