import pytest

from src.masks import get_mask_card_number, get_mask_account


#@pytest.mark.parametrize("number_card, mask_number", [("1234567891234567", "1234 56** **** 4567"),
#                                                       ("7000792289606361', '7000 79** **** 6361"),
#                                                       ("2200240497191490', '2200 24** **** 1490"), ])
def test_get_mask_card_number():
    assert get_mask_card_number('7000792289606361') == '7000 79** **** 6361'
    assert get_mask_card_number('4324ji') == 'Некоректный номер карты. Введите 16-значный номер'


@pytest.mark.parametrize("account, mask_account", [("73654108430135874305", "**4305"), ])
def test_get_mask_account():
    assert get_mask_account('73654108430135874305') == '**4305'
