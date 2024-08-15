import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize("number_card, mask_number", [("1234567891234567", "1234 56** **** 4567"),
                                                      ("7000792289606361", "7000 79** **** 6361"),
                                                      ("2200240497191490", "2200 24** **** 1490"),
                                                      ('70007922896063611', ''),
                                                      ('700079228960636', ''),
                                                      ('70007922896063ab', '')
                                                      ])
def test_get_mask_card_number(number_card, mask_number):
    """Тест для проверки функции маскировки номера банковской карты"""
    assert get_mask_card_number('7000792289606361') == '7000 79** **** 6361'
    assert get_mask_card_number('7000792289606362') == '7000 79** **** 6362'


@pytest.mark.parametrize("account, mask_account", [("73654108430135874305", "**4305"),
                                                   ('736541084301358743051', ''),
                                                   ('7365410843013587430', ''),
                                                   ('736541084301358743ab', '')
                                                   ])
def test_get_mask_account(account, mask_account):
    """Тест для проверки функции маскировки банковского счета"""
    assert get_mask_account('73654108430135874305') == '**4305'
    assert get_mask_account('73654108430135874306') == '**4306'
