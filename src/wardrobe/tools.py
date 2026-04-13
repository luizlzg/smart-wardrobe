"""
Tool definitions for the wardrobe multi-agent system.

All tools use ToolRuntime for state reads and return Command for state writes.
Tool lists are defined as module-level constants at the bottom of the file.
"""

# TODO: implement tools
# Planned tools:
#   - analyze_clothing_image   : vision call → category + raw description
#   - enrich_description       : merge user description into AI description
#   - lookup_wardrobe          : read clothing descriptions from knowledge base
#   - suggest_outfit_items     : pick items that match the outfit context
#   - ask_interview_question   : emit the next strategic style question
#   - record_style_signal      : write a new style signal into the profile store
#   - merge_style_profile      : background merge of recent_events into profile

CLOTHING_ANALYSIS_TOOLS: list = []
OUTFIT_SUGGESTION_TOOLS: list = []
PROFILE_INTERVIEW_TOOLS: list = []
MEMORY_UPDATE_TOOLS: list = []
