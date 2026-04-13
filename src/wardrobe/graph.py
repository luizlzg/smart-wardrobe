"""
StateGraph wiring and compilation for the wardrobe system.

build_graph() always accepts checkpointer=None — callers decide whether to
pass one (e.g. MemorySaver for multi-turn interview flows).
"""

from langgraph.graph import END, START, StateGraph

from src.wardrobe.agent_definition import (
    clothing_analysis_node,
    memory_update_node,
    outfit_suggestion_node,
    profile_interview_node,
)
from src.wardrobe.state import GraphState


def build_clothing_analysis_graph(checkpointer=None):
    # TODO: implement
    raise NotImplementedError


def build_outfit_suggestion_graph(checkpointer=None):
    # TODO: implement
    raise NotImplementedError


def build_profile_interview_graph(checkpointer=None):
    # TODO: implement — multi-turn, needs MemorySaver at call site
    raise NotImplementedError


def build_memory_update_graph(checkpointer=None):
    # TODO: implement — stateless one-shot, no checkpointer needed
    raise NotImplementedError
