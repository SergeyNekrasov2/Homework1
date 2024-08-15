from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(nums: str) -> str | None:
    """Функция общей маскировки карты и счёта"""
    if len(nums) == 20:
        return f'Счет {get_mask_account(nums)}'
    else:
        cards = get_mask_card_number(nums[-16:])
        new_card = nums.replace(nums[-16:], cards)
        return new_card


# print(mask_account_card('73654108430135874305'))
# print(mask_account_card('Visa Platinum 7000792289606361'))
# print(mask_account_card('Maestro 7000792289606361'))


def get_data(date: str) -> str | None:
    """Функция преобразования даты"""
    return f'{date[8:10]}.{date[5:7]}.{date[0:4]}'


print(get_data('2024-07-26T04:32:20.612820'))
# print(get_data('2024-07-26T04:32:20.612820'))
