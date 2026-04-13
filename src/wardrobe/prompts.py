"""
System prompt constants — one per agent.

Each prompt must cover:
  1. Identity   — what the agent is and its single responsibility
  2. Tools      — every tool with signature and usage example
  3. Workflow   — numbered steps if call order matters
  4. Rules      — constraints, edge cases, what not to do
  5. Output     — what the structured response must contain

Runtime values are injected via .format(language=..., ...) in the node function.
"""

# TODO: implement prompts
CLOTHING_ANALYSIS_PROMPT: str = ""
OUTFIT_SUGGESTION_PROMPT: str = ""
PROFILE_INTERVIEW_PROMPT: str = ""
MEMORY_UPDATE_PROMPT: str = ""
