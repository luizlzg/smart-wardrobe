import os


def setup_langsmith_tracing() -> None:
    api_key = os.getenv("LANGSMITH_API_KEY")
    if not api_key:
        return

    tracing = os.getenv("LANGSMITH_TRACING", "").lower()
    if tracing not in ("true", "1", "yes"):
        return

    os.environ.setdefault("LANGSMITH_PROJECT", "smart-wardrobe")
    os.environ.setdefault("LANGSMITH_ENDPOINT", "https://api.smith.langchain.com")
