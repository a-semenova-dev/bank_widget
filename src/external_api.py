"""
Модуль для конвертации валют через внешнее API.
"""

import os
from typing import Dict, Any

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
        f"https://api.apilayer.com/exchangerates_data/convert?"
        f"to=RUB&from={currency}&amount={amount}"
    )

    response = requests.get(url, headers={"apikey": api_key})

    if response.status_code != 200:
        return 0.0

    data = response.json()
    result = data.get("result", 0.0)
    return float(result)
