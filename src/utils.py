import json
from typing import Any, Dict, List

from src.logger_config import setup_logger

logger = setup_logger("utils", "utils.log")


def read_transactions_from_json(file_path: str) -> List[Dict[str, Any]]:
    logger.info(f"Reading file: {file_path}")
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, list):
                logger.info(f"Loaded {len(data)} transactions")
                return data
            else:
                logger.warning(f"File {file_path} is not a list")
                return []
    except FileNotFoundError:
        logger.error(f"File not found: {file_path}")
        return []
    except json.JSONDecodeError as e:
        logger.error(f"JSON decode error: {e}")
        return []
