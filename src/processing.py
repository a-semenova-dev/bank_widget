"""
Модуль для фильтрации и сортировки банковских операций.
"""

from typing import List, Dict, Any


def filter_by_state(transactions: List[Dict[str, Any]], state: str = 'EXECUTED') -> List[Dict[str, Any]]:
    """
    Фильтрует список транзакций по значению ключа 'state'.

    Аргументы:
        transactions (List[Dict[str, Any]]): Список словарей с данными о транзакциях.
        state (str): Значение поля 'state' для фильтрации. По умолчанию 'EXECUTED'.

    Возвращает:
        List[Dict[str, Any]]: Новый список, содержащий только транзакции с указанным состоянием.
    """
    return [item for item in transactions if item.get('state') == state]


def sort_by_date(transactions: List[Dict[str, Any]], descending: bool = True) -> List[Dict[str, Any]]:
    """
    Сортирует список транзакций по дате.

    Аргументы:
        transactions (List[Dict[str, Any]]): Список словарей с данными о транзакциях.
        descending (bool): Если True — сортировка по убыванию (сначала новые).
                           Если False — по возрастанию (сначала старые).

    Возвращает:
        List[Dict[str, Any]]: Новый список транзакций, отсортированный по дате.
    """
    return sorted(transactions, key=lambda x: x['date'], reverse=descending)