"""
Модуль для чтения финансовых транзакций из CSV и Excel файлов.
"""

from typing import Dict, List

import pandas as pd


def read_transactions_from_csv(file_path: str) -> List[Dict]:
    """
    Читает CSV-файл и возвращает список словарей с транзакциями.

    Аргументы:
        file_path (str): Путь к CSV-файлу.

    Возвращает:
        List[Dict]: Список транзакций.
    """
    try:
        df = pd.read_csv(file_path)
        return df.to_dict(orient="records")
    except Exception:
        return []


def read_transactions_from_excel(file_path: str) -> List[Dict]:
    """
    Читает Excel-файл и возвращает список словарей с транзакциями.

    Аргументы:
        file_path (str): Путь к Excel-файлу.

    Возвращает:
        List[Dict]: Список транзакций.
    """
    try:
        df = pd.read_excel(file_path)
        return df.to_dict(orient="records")
    except Exception:
        return []
