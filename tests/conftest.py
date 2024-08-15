import pytest


@pytest.fixture
def number_card(mask_number):
    return '7000 79** **** 6361'


@pytest.fixture
def account(mask_account):
    return '**4305'
