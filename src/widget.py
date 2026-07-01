from datetime import datetime

    name_part, number_part = parts
    if not number_part.isdigit():
        raise ValueError("Номер должен состоять только из цифр")
    if len(number_part) == 16:
        masked_number = get_mask_card_number(number_part)
    elif len(number_part) > 16:
        masked_number = get_mask_account(number_part)
    else:

    return f"{name_part} {masked_number}"


def get_date(date_string: str) -> str:
    date_obj = datetime.fromisoformat(date_string)
