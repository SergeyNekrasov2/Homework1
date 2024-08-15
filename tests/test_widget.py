import pytest

from src.widget import get_data, mask_account_card


@pytest.mark.parametrize("nums, mask_nums", [("73654108430135874305", "Счет **4305"),
                                             ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
                                             ("Maestro 7000792289606361", "Maestro 7000 79** **** 6361"), ])
def test_mask_account_card(nums, mask_nums):
    """Тест для проверки функции общей маскировки банковского счета и номера банковской карты"""
    assert mask_account_card(nums) == mask_nums


@pytest.mark.parametrize("data, date", [('2024-07-26T04:32:20.612820', '26.07.2024'), ])
def test_get_data(data, date):
    """Тест для проверки функции расшифровки даты"""
    assert get_data(data) == date
