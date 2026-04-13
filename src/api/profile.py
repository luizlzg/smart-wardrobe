"""
Profile / style-memory endpoints.

AI features handled here:
- Onboarding interview: a conversational AI asks strategic questions to
  build the user's initial style profile (preferences, occasions, vibe, etc.)
  before they have enough outfit history to infer taste automatically.
- Memory update (background): a routine that runs after outfit sessions and
  feedback events to incrementally refine the stored style profile.
"""

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class InterviewMessageRequest(BaseModel):
    user_id: str
    session_id: str | None = None  # None = start a new interview session
    message: str  # user's reply to the AI question


class MemoryUpdateRequest(BaseModel):
    user_id: str
    # Triggered after outfit feedback or at session close
    # Payload contains recent interactions to be processed
    recent_events: list[dict]


@router.post("/interview")
async def profile_interview(body: InterviewMessageRequest):
    """
    Multi-turn conversational endpoint for the initial style-profile interview.

    On the first call (session_id=None) the AI opens with the first strategic
    question. Subsequent calls continue the conversation until the profile is
    considered complete. Returns the AI's next question (or a completion
    signal) plus the current session ID.
    """
    # TODO: implement
    raise NotImplementedError


@router.post("/memory/update")
async def update_style_memory(body: MemoryUpdateRequest):
    """
    Background routine endpoint — called server-side after outfit sessions or
    feedback events. Processes recent interactions and merges new style signals
    into the persistent user profile.

    Can be triggered by a queue worker or a scheduled job; not called directly
    by the mobile client.
    """
    # TODO: implement
    raise NotImplementedError


@router.get("/{user_id}")
async def get_profile(user_id: str):
    """
    Return the current style profile for a user (read-only, for debugging
    and display purposes).
    """
    # TODO: implement
    raise NotImplementedError
