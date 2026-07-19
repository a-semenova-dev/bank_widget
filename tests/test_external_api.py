"""
Тесты для модуля external_api.
"""

import os
import pytest
from unittest.mock import patch, Mock
from src.external_api import convert_to_rubles


def test_convert_rub_to_rub():
    """Тест: конвертация RUB в RUB (без API)."""
    transaction = {
        "operationAmount": {
            "amount": "100.00",
            "currency": {"code": "RUB"}
        }
    }
    result = convert_to_rubles(transaction)
    assert result == 100.00


@patch("src.external_api.requests.get")
def test_convert_usd_to_rub_success(mock_get):
    """Тест: успешная конвертация USD → RUB."""
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"rates": {"RUB": 75.0}}
    mock_get.return_value = mock_response

    os.environ["EXCHANGE_RATE_API_KEY"] = "test_key"

    transaction = {
        "operationAmount": {
            "amount": "10.00",
            "currency": {"code": "USD"}
        }
    }
    result = convert_to_rubles(transaction)
    assert result == 750.0


@patch("src.external_api.requests.get")
def test_convert_eur_to_rub_success(mock_get):
    """Тест: успешная конвертация EUR → RUB."""
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"rates": {"RUB": 85.0}}
    mock_get.return_value = mock_response

    os.environ["EXCHANGE_RATE_API_KEY"] = "test_key"

    transaction = {
        "operationAmount": {
            "amount": "10.00",
            "currency": {"code": "EUR"}
        }
    }
    result = convert_to_rubles(transaction)
    assert result == 850.0


def test_convert_no_api_key():
    """Тест: API-ключ отсутствует."""
    if "EXCHANGE_RATE_API_KEY" in os.environ:
        del os.environ["EXCHANGE_RATE_API_KEY"]

    transaction = {
        "operationAmount": {
            "amount": "10.00",
            "currency": {"code": "USD"}
        }
    }
    result = convert_to_rubles(transaction)
    assert result == 0.0


@patch("src.external_api.requests.get")
def test_convert_api_error(mock_get):
    """Тест: ошибка при запросе к API."""
    mock_response = Mock()
    mock_response.status_code = 500
    mock_get.return_value = mock_response

    os.environ["EXCHANGE_RATE_API_KEY"] = "test_key"

    transaction = {
        "operationAmount": {
            "amount": "10.00",
            "currency": {"code": "USD"}
        }
    }
    result = convert_to_rubles(transaction)
    assert result == 0.0


@patch("src.external_api.requests.get")
def test_convert_invalid_api_response(mock_get):
    """Тест: невалидный ответ от API."""
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {}  # нет ключа "rates"
    mock_get.return_value = mock_response

    os.environ["EXCHANGE_RATE_API_KEY"] = "test_key"

    transaction = {
        "operationAmount": {
            "amount": "10.00",
            "currency": {"code": "USD"}
        }
    }
    result = convert_to_rubles(transaction)
    assert result == 0.0