"""
Модуль для работы с JSON-файлами.
"""

import json
from typing import Any, Dict, List


def read_transactions_from_json(file_path: str) -> List[Dict[str, Any]]:
    """
    Читает JSON-файл и возвращает список словарей с транзакциями.

    Аргументы:
        file_path (str): Путь к JSON-файлу.

    Возвращает:
        List[Dict[str, Any]]: Список транзакций или пустой список при ошибке.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
            else:
                return []
    except (FileNotFoundError, json.JSONDecodeError):
        return []
