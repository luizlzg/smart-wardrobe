# Smart Wardrobe

AI-powered digital wardrobe and outfit builder.

## What it does

- **Clothing registration** — upload a photo and the AI automatically categorizes the item and generates a detailed description (color, brand, style, details). An optional user description is merged in to enrich the output.
- **Outfit suggestion** — describe the occasion and the AI navigates your wardrobe to suggest a complete outfit, tailored to your personal style profile.
- **Style profiling** — a conversational AI runs a short interview on first use to capture your preferences. A background routine keeps refining the profile as you interact.
- **Outfit sharing** — save and share outfit combinations (no affiliate links in MVP).

## Stack

| Layer | Technology |
|---|---|
| API | FastAPI |
| Orchestration | LangGraph 1.0+ |
| Agents | LangChain 1.0+ |
| LLM | OpenRouter via `ChatOpenAI` |
| Package manager | [uv](https://docs.astral.sh/uv/) |

## Project structure

```
smart-wardrobe/
├── main.py                     # FastAPI entry point + env validation
├── pyproject.toml              # uv-managed dependencies
└── src/
    ├── api/
    │   ├── clothing.py         # POST /clothing/analyze
    │   ├── outfit.py          # POST /outfit/suggest, /feedback, /share
    │   └── profile.py         # POST /profile/interview, /memory/update · GET /profile/{id}
    ├── wardrobe/               # LangGraph agent system
    │   ├── state.py           # GraphState TypedDict + output schemas
    │   ├── tools.py           # @tool functions + tool lists per agent
    │   ├── prompts.py         # System prompt constants per agent
    │   ├── agent_definition.py # Agent creation + node functions
    │   ├── graph.py           # StateGraph wiring and compilation
    │   └── other_nodes.py     # Non-LLM nodes (routers, builders)
    ├── middleware/             # Shared validation middleware
    └── utils/
        ├── logger.py          # Pre-configured LOGGER
        └── observability.py   # LangSmith tracing setup
```

## AI endpoints

| Method | Path | What the AI does |
|---|---|---|
| `POST` | `/clothing/analyze` | Vision model categorizes item + generates description from photo |
| `POST` | `/outfit/suggest` | Reads wardrobe KB + style profile → picks a full outfit for the given context |
| `POST` | `/outfit/feedback` | Records like/dislike; feeds the background memory update |
| `POST` | `/outfit/share` | Generates a shareable outfit card |
| `POST` | `/profile/interview` | Multi-turn conversation to build initial style profile |
| `POST` | `/profile/memory/update` | Background routine — merges recent events into stored profile |
| `GET` | `/profile/{user_id}` | Returns the current style profile |

## Getting started

```bash
# Install dependencies
uv sync

# Copy and fill in required env vars
cp .env.example .env

# Run the API
uv run python main.py
```

## Environment variables

**Required:**

```
OPENROUTER_API_KEY
```

**Per-agent model overrides** (fall back to `anthropic/claude-sonnet-4-20250514`):

```
CLOTHING_ANALYSIS_MODEL
OUTFIT_SUGGESTION_MODEL
PROFILE_INTERVIEW_MODEL
MEMORY_UPDATE_MODEL
```

**Optional — observability:**

```
LANGSMITH_API_KEY
LANGSMITH_TRACING=true
LANGSMITH_PROJECT=smart-wardrobe
```

## MVP scope

In scope: clothing registration, AI categorization + description, outfit builder (manual + AI), style profile interview, background memory update, outfit sharing.

Out of scope for now: affiliate links, resale value tracking, virtual try-on, creator monetization.
