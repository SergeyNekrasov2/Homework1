def get_mask_card_number(card_number: str) -> str | None:
    """Возвращает замаскированный номер карты в виде строки"""
    if card_number.isdigit() and len(card_number) == 16:
        return f"{card_number[:4]} {card_number[4:6]}{'*' * 2} {'*' * 4} {card_number[12:]}"
    else:
        return None


# print(get_mask_card_number('7000792289606361'))


def get_mask_account(acc_number: str) -> str | None:
    """Возвращает замаскированный номер счета в виде строки"""
    if acc_number.isdigit() and len(acc_number) == 20:
        return f"{'*' * 2}{acc_number[-4::]}"
    else:
        return None
# print(get_mask_account('73654108430135874305'))
# print('Счет', get_mask_account('73654108430135874305'))
