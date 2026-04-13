"""
Agent creation functions and node functions for the wardrobe system.

One create_*_agent() function per agent.
One *_node() function per graph node.
"""

import os

from src.wardrobe.state import GraphState

# ---------------------------------------------------------------------------
# Clothing Analysis Agent
# Multimodal: receives clothing photo → outputs category + description.
# ---------------------------------------------------------------------------


def create_clothing_analysis_agent(model_name: str | None = None, language: str = "pt"):
    # TODO: implement
    raise NotImplementedError


def clothing_analysis_node(state: GraphState) -> dict:
    # TODO: implement
    raise NotImplementedError


# ---------------------------------------------------------------------------
# Outfit Suggestion Agent
# Reads wardrobe knowledge base + style profile → suggests a complete outfit.
# ---------------------------------------------------------------------------


def create_outfit_suggestion_agent(model_name: str | None = None, language: str = "pt"):
    # TODO: implement
    raise NotImplementedError


def outfit_suggestion_node(state: GraphState) -> dict:
    # TODO: implement
    raise NotImplementedError


# ---------------------------------------------------------------------------
# Profile Interview Agent
# Conversational: asks strategic questions to build the initial style profile.
# ---------------------------------------------------------------------------


def create_profile_interview_agent(model_name: str | None = None, language: str = "pt"):
    # TODO: implement
    raise NotImplementedError


def profile_interview_node(state: GraphState) -> dict:
    # TODO: implement
    raise NotImplementedError


# ---------------------------------------------------------------------------
# Memory Update Agent
# Background: merges recent interaction events into the stored style profile.
# ---------------------------------------------------------------------------


def create_memory_update_agent(model_name: str | None = None, language: str = "pt"):
    # TODO: implement
    raise NotImplementedError


def memory_update_node(state: GraphState) -> dict:
    # TODO: implement
    raise NotImplementedError
