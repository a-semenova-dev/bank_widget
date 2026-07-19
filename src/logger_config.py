import logging
import os
from typing import Optional


def setup_logger(name: str, log_file: Optional[str] = None) -> logging.Logger:
    if log_file is None:
        log_file = f"{name}.log"

    os.makedirs("logs", exist_ok=True)

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    if logger.handlers:
        return logger

    file_handler = logging.FileHandler(f"logs/{log_file}", mode="w")
    file_handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger
