
from typing import Generator, Dict, Any, Iterator


def filter_by_currency(
    transactions: list[Dict[str, Any]],
    currency: str
) -> Generator[Dict[str, Any], None, None]:

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

    for transaction in transactions:
        yield transaction.get("description", "")


def card_number_generator(start: int, stop: int) -> Iterator[str]:

    for number in range(start, stop + 1):
        card_str = f"{number:016d}"
        formatted = (
            f"{card_str[:4]} {card_str[4:8]} {card_str[8:12]} {card_str[12:]}"
        )
        yield formatted
