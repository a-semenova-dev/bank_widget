"""
Модуль для работы с генераторами транзакций.
"""


def filter_by_currency(transactions, currency):
    """
    Возвращает итератор с транзакциями, где валюта соответствует заданной.

    Аргументы:
        transactions (list): Список словарей с транзакциями.
        currency (str): Код валюты (например, "USD").

    Возвращает:
        generator: Итератор с отфильтрованными транзакциями.
    """
    for transaction in transactions:
        if (
            transaction.get("operationAmount", {})
            .get("currency", {})
            .get("code") == currency
        ):
            yield transaction


def transaction_descriptions(transactions):
    """
    Генерирует описания транзакций по очереди.

    Аргументы:
        transactions (list): Список словарей с транзакциями.

    Возвращает:
        generator: Описание каждой транзакции.
    """
    for transaction in transactions:
        yield transaction.get("description", "")


def card_number_generator(start, stop):
    """
    Генерирует номера карт в заданном диапазоне в формате XXXX XXXX XXXX XXXX.

    Аргументы:
        start (int): Начальное значение диапазона.
        stop (int): Конечное значение диапазона (включительно).

    Возвращает:
        generator: Номера карт в формате с пробелами.
    """
    for number in range(start, stop + 1):
        card_str = f"{number:016d}"
        formatted = (
            f"{card_str[:4]} {card_str[4:8]} {card_str[8:12]} {card_str[12:]}"
        )
        yield formatted
