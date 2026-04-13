"""
Non-LLM nodes: routers, reducers, and builders for the wardrobe graph.
"""

from src.wardrobe.state import GraphState


def error_router(state: GraphState) -> str:
    """Route to END on invalid input, otherwise continue the happy path."""
    # TODO: implement
    raise NotImplementedError


def wardrobe_kb_builder_node(state: GraphState) -> dict:
    """
    Non-LLM node that assembles the wardrobe knowledge base payload for the
    outfit suggestion agent — reads persisted clothing descriptions and packs
    them into state so the agent doesn't need direct DB access.
    """
    # TODO: implement
    raise NotImplementedError
