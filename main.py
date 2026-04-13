import os

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI

from src.api.clothing import router as clothing_router
from src.api.outfit import router as outfit_router
from src.api.profile import router as profile_router
from src.utils.observability import setup_langsmith_tracing

load_dotenv()


def _check_env_vars(required: list[str]):
    missing = [k for k in required if not os.getenv(k)]
    if missing:
        raise EnvironmentError(f"Missing required env vars: {missing}")


_check_env_vars(["OPENROUTER_API_KEY"])

setup_langsmith_tracing()

app = FastAPI(
    title="Smart Wardrobe API",
    description="AI-powered digital wardrobe and outfit builder",
    version="0.1.0",
)

app.include_router(clothing_router, prefix="/clothing", tags=["clothing"])
app.include_router(outfit_router, prefix="/outfit", tags=["outfit"])
app.include_router(profile_router, prefix="/profile", tags=["profile"])


@app.get("/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
