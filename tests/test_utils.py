"""
Тесты для модуля utils.
"""

import json
import pytest
from src.utils import read_transactions_from_json


def test_read_transactions_success(tmp_path):
    """Тест успешного чтения JSON-файла."""
    test_data = [
        {
            "id": 1,
            "state": "EXECUTED",
            "date": "2025-01-01",
            "operationAmount": {
                "amount": "100.50",
                "currency": {"name": "USD", "code": "USD"}
            },
            "description": "Перевод"
        }
    ]

    file_path = tmp_path / "operations.json"
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(test_data, f)

    result = read_transactions_from_json(str(file_path))
    assert result == test_data


def test_read_transactions_not_found():
    """Тест: файл не найден."""
    result = read_transactions_from_json("non_existent_file.json")
    assert result == []


def test_read_transactions_not_list(tmp_path):
    """Тест: содержимое файла не является списком."""
    file_path = tmp_path / "not_list.json"
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump({"key": "value"}, f)

    result = read_transactions_from_json(str(file_path))
    assert result == []


def test_read_transactions_invalid_json(tmp_path):
    """Тест: невалидный JSON."""
    file_path = tmp_path / "invalid.json"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write("{invalid}")

    result = read_transactions_from_json(str(file_path))
    assert result == []


def test_read_transactions_empty_file(tmp_path):
    """Тест: пустой файл."""
    file_path = tmp_path / "empty.json"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write("")

    result = read_transactions_from_json(str(file_path))
    assert result == []