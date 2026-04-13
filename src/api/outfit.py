"""
Outfit endpoints.

AI features handled here:
- Outfit suggestion: given a user context (e.g. "going to a bar with friends
  tonight"), the AI reads the wardrobe knowledge base (clothing descriptions
  + categories) and picks a complete outfit that fits both the context and
  the user's style profile.
- Iterative feedback: the user can like/dislike a suggestion and ask for
  another one within the same session.
"""

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class OutfitSuggestRequest(BaseModel):
    user_id: str
    context: str  # e.g. "balada com amigos", "reunião de trabalho"
    session_id: str | None = None  # reuse for multi-turn feedback


class OutfitFeedbackRequest(BaseModel):
    session_id: str
    liked: bool
    feedback_text: str | None = None  # optional written feedback


@router.post("/suggest")
async def suggest_outfit(body: OutfitSuggestRequest):
    """
    Return an outfit suggestion for the given user context.

    The AI navigates the user's wardrobe descriptions + style profile and
    picks a set of clothing items that match the occasion and personal taste.
    Responds with the selected items and a brief styling note.
    """
    # TODO: implement
    raise NotImplementedError


@router.post("/feedback")
async def outfit_feedback(body: OutfitFeedbackRequest):
    """
    Accept user feedback on the last suggestion and optionally return a new
    one. Feedback is also fed into the background memory-update routine.
    """
    # TODO: implement
    raise NotImplementedError


@router.post("/share")
async def share_outfit(outfit_id: str):
    """
    Generate a shareable link/card for a saved outfit.
    (No affiliate links for MVP — just social sharing.)
    """
    # TODO: implement
    raise NotImplementedError
