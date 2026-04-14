from pathlib import Path
from loguru import logger

Path("logs").mkdir(parents=True, exist_ok=True)

logger.add(
    "logs/app.log",
    rotation="10 MB",
    retention="7 days",
    level="INFO",
    enqueue=False,
)
