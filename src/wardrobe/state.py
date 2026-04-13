"""
Shared graph state and output schemas for the wardrobe multi-agent system.
"""

import operator
from typing import Annotated, Any
from langchain.agents import AgentState
from typing_extensions import TypedDict


class GraphState(AgentState):
    # Conversation history — appended by every node
    messages: Annotated[list[Any], operator.add]

    # Runtime context
    user_id: str
    language: str
    api_mode: bool  # True = interrupt propagates to caller; False = handled inline

    # Flow control
    invalid_input: bool
    error_message: str

    # --- Clothing analysis ---
    # Inputs
    clothing_photo_bytes: bytes | None
    user_description: str  # optional extra description from user

    # Outputs
    clothing_category: str
    clothing_description: str  # AI-generated, enriched by user_description

    # --- Outfit suggestion ---
    outfit_context: str  # e.g. "balada com amigos"
    session_id: str | None
    suggested_outfit: dict  # {items: [...], styling_note: str}

    # --- Profile / interview ---
    interview_session_id: str | None
    interview_complete: bool
    style_profile: dict  # accumulated style signals

    # --- Memory update ---
    recent_events: list[dict]  # outfit feedback + interaction history
