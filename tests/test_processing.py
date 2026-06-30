import pytest
from src.processing import filter_by_state, sort_by_date

@pytest.fixture
def sample_transactions():
    return [
        {"id": 1, "state": "EXECUTED", "date": "2025-01-01"},
        {"id": 2, "state": "CANCELED", "date": "2024-12-01"},
        {"id": 3, "state": "EXECUTED", "date": "2025-02-01"},
    ]

def test_filter_by_state(sample_transactions):
    result = filter_by_state(sample_transactions)
    assert len(result) == 2
    assert all(item["state"] == "EXECUTED" for item in result)

def test_filter_by_state_canceled(sample_transactions):
    result = filter_by_state(sample_transactions, "CANCELED")
    assert len(result) == 1
    assert result[0]["id"] == 2

def test_filter_by_state_empty():
    assert filter_by_state([]) == []

def test_sort_by_date(sample_transactions):
    result = sort_by_date(sample_transactions)
    assert result[0]["date"] == "2025-02-01"
    assert result[1]["date"] == "2025-01-01"
    assert result[2]["date"] == "2024-12-01"

def test_sort_by_date_ascending(sample_transactions):
    result = sort_by_date(sample_transactions, descending=False)
    assert result[0]["date"] == "2024-12-01"
    assert result[1]["date"] == "2025-01-01"
    assert result[2]["date"] == "2025-02-01"
