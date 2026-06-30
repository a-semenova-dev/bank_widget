"""
Тесты для модуля generators.
"""

import pytest
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


@pytest.fixture
def sample_transactions():
    """Фикстура с транзакциями для тестов."""
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {"name": "USD", "code": "USD"}
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {"name": "USD", "code": "USD"}
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {"name": "руб.", "code": "RUB"}
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        }
    ]


def test_filter_by_currency_usd(sample_transactions):
    """Тест фильтрации по USD."""
    usd_transactions = list(filter_by_currency(sample_transactions, "USD"))
    assert len(usd_transactions) == 2
    for transaction in usd_transactions:
        assert transaction["operationAmount"]["currency"]["code"] == "USD"


def test_filter_by_currency_rub(sample_transactions):
    """Тест фильтрации по RUB."""
    rub_transactions = list(filter_by_currency(sample_transactions, "RUB"))
    assert len(rub_transactions) == 1
    for transaction in rub_transactions:
        assert transaction["operationAmount"]["currency"]["code"] == "RUB"


def test_filter_by_currency_not_found(sample_transactions):
    """Тест фильтрации по отсутствующей валюте."""
    eur_transactions = list(filter_by_currency(sample_transactions, "EUR"))
    assert len(eur_transactions) == 0


def test_filter_by_currency_empty_list():
    """Тест фильтрации по пустому списку."""
    empty_transactions = list(filter_by_currency([], "USD"))
    assert len(empty_transactions) == 0

def test_transaction_descriptions(sample_transactions):
    """Тест получения описаний транзакций."""
    descriptions = list(transaction_descriptions(sample_transactions))
    expected = [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет"
    ]
    assert descriptions == expected


def test_transaction_descriptions_empty():
    """Тест получения описаний из пустого списка."""
    descriptions = list(transaction_descriptions([]))
    assert descriptions == []

def test_card_number_generator_range():
    """Тест генерации номеров карт в диапазоне."""
    cards = list(card_number_generator(1, 5))
    expected = [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
        "0000 0000 0000 0004",
        "0000 0000 0000 0005"
    ]
    assert cards == expected


def test_card_number_generator_single():
    """Тест генерации одного номера карты."""
    cards = list(card_number_generator(9999, 9999))
    assert cards == ["0000 0000 0000 9999"]


def test_card_number_generator_large():
    """Тест генерации номера с большим числом."""
    cards = list(card_number_generator(9999999999999999, 9999999999999999))
    assert cards == ["9999 9999 9999 9999"]