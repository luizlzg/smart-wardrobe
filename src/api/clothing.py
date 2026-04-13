"""
Clothing endpoints.

AI features handled here:
- Multimodal categorization: AI receives the clothing photo and picks the
  correct category from a predefined list (no manual selection by the user).
- Description generation: AI describes the item in detail (color, brand,
  style, details). An optional user-provided description is merged in to
  enrich the AI output.
"""

from fastapi import APIRouter, File, Form, UploadFile

router = APIRouter()


@router.post("/analyze")
async def analyze_clothing(
    photo: UploadFile = File(...),
    user_description: str = Form(default=""),
):
    """
    Receive a clothing photo and return:
    - category  (AI-generated, e.g. "camiseta", "calça jeans", "blazer")
    - description  (detailed AI-generated text, optionally enriched by
                    `user_description`)

    The clothing ID and its description are persisted so the Outfit Builder
    can later navigate the wardrobe without needing the raw images.
    """
    # TODO: implement
    raise NotImplementedError
