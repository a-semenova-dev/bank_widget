"""
Модуль для конвертации валют через внешнее API.
"""

import os
from typing import Any, Dict

import requests


def convert_to_rubles(transaction: Dict[str, Any]) -> float:
    """
    Конвертирует сумму транзакции в рубли.

    Аргументы:
        transaction (Dict[str, Any]): Словарь с данными о транзакции.

    Возвращает:
        float: Сумма в рублях.
    """
    amount = float(transaction.get("operationAmount", {}).get("amount", 0))
    currency = (
        transaction.get("operationAmount", {})
        .get("currency", {})
        .get("code", "RUB")
    )

    if currency == "RUB":
        return amount

    api_key = os.getenv("EXCHANGE_RATE_API_KEY")
    if not api_key:
        return 0.0

    url = (
        "https://api.exchangeratesapi.io/latest?"
        f"base={currency}&symbols=RUB"
    )
    response = requests.get(url, headers={"apikey": api_key})

    if response.status_code != 200:
        return 0.0

    data = response.json()
    rate = data.get("rates", {}).get("RUB", 0)
    return float(amount * rate)
