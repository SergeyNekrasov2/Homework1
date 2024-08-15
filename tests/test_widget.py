import pytest

from src.widget import mask_account_card, get_data


@pytest.mark.parametrize("nums, mask_nums", [("73654108430135874305", "Счет **4305"),
                                             ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
                                             ("Maestro 7000792289606361", "Maestro 7000 79** **** 6361"), ])
def test_mask_account_card(nums, mask_nums):
    """Тест для проверки функции общей маскировки банковского счета и номера банковской карты"""
    assert mask_account_card('73654108430135874305') == 'Счет **4305'
    assert mask_account_card('Visa Platinum 7000792289606361') == 'Visa Platinum 7000792289606361'
    assert mask_account_card('Maestro 7000792289606361') == 'Maestro 7000 79** **** 6361'


# @pytest.mark.parametrize("account, mask_account", [("73654108430135874305", "**4305"), ])
def test_get_data(data, date):
    """Тест для проверки функции расшифровки даты"""
    assert get_data('2024-07-26T04:32:20.612820') == '26.07.2024'
    assert get_data('2024-08-26T04:32:20.612820') == '26.08.2024'
