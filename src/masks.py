def get_mask_card_number(card_number: str) -
    if len(card_number) != 16 or not card_number.isdigit(): 
        raise ValueError("Номер карты должен содержать ровно 16 цифр") 
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}" 
 
def get_mask_account(account_number: str) -
        raise ValueError("Номер счета должен содержать минимум 4 цифры") 
    return f"**{account_number[-4:]}" 
