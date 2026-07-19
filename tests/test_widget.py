import pytest
from src.widget import mask_account_card, get_date


@pytest.mark.parametrize("input_str, expected", [
    ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
    ("Счет 73654108430135874305", "Счет **4305"),
])
def test_mask_account_card(input_str, expected):
    assert mask_account_card(input_str) == expected


def test_mask_account_card_invalid():
    with pytest.raises(ValueError):
        mask_account_card("Invalid")


def test_get_date():
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"
