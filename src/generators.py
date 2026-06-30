"""
Модуль для работы с генераторами транзакций.
"""
from typing import Generator, Dict, Any, Iterator


def filter_by_currency(
    transactions: list[Dict[str, Any]],
    currency: str
) -> Generator[Dict[str, Any], None, None]:
    """
    Возвращает итератор с транзакциями, где валюта соответствует заданной.

    Аргументы:
        transactions (list[Dict[str, Any]]): Список словарей с транзакциями.
        currency (str): Код валюты (например, "USD").

    Возвращает:
        Generator[Dict[str, Any], None, None]: Итератор с отфильтрованными транзакциями.
    """
    for transaction in transactions:
        if (
            transaction.get("operationAmount", {})
            .get("currency", {})
            .get("code") == currency
        ):
            yield transaction


def transaction_descriptions(
    transactions: list[Dict[str, Any]]
) -> Generator[str, None, None]:
    """
    Генерирует описания транзакций по очереди.

    Аргументы:
        transactions (list[Dict[str, Any]]): Список словарей с транзакциями.

    Возвращает:
        Generator[str, None, None]: Описание каждой транзакции.
    """
    for transaction in transactions:
        yield transaction.get("description", "")


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """
    Генерирует номера карт в заданном диапазоне в формате XXXX XXXX XXXX XXXX.

    Аргументы:
        start (int): Начальное значение диапазона.
        stop (int): Конечное значение диапазона (включительно).

    Возвращает:
        Iterator[str]: Номера карт в формате с пробелами.
    """
    for number in range(start, stop + 1):
        card_str = f"{number:016d}"
        formatted = (
            f"{card_str[:4]} {card_str[4:8]} {card_str[8:12]} {card_str[12:]}"
        )
        yield formatted
