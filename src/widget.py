from datetime import datetime
from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(card_or_account: str) -> str:
    parts = card_or_account.rsplit(' ', 1)
    if len(parts) != 2:
        raise ValueError("Неверный формат: ожидается название и номер через пробел")
    name_part, number_part = parts
    if not number_part.isdigit():
        raise ValueError("Номер должен состоять только из цифр")
    if len(number_part) == 16:
        masked_number = get_mask_card_number(number_part)
    elif len(number_part) > 16:
        masked_number = get_mask_account(number_part)
    else:
        raise ValueError("Номер должен содержать 16 цифр (карта) или больше 16 (счёт)")
    return f"{name_part} {masked_number}"


def get_date(date_string: str) -> str:
    date_obj = datetime.fromisoformat(date_string)
    return date_obj.strftime("%d.%m.%Y")