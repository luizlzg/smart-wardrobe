import logging
import os
from datetime import datetime
from pathlib import Path

_LOG_DIR = Path(".logs")
_LOG_DIR.mkdir(exist_ok=True)

_timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
_log_file = _LOG_DIR / f"smart_wardrobe_{_timestamp}.log"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s — %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler(_log_file, encoding="utf-8"),
    ],
)

LOGGER = logging.getLogger("smart_wardrobe")
