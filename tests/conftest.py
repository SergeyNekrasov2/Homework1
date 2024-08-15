import pytest


@pytest.fixture
def number_card(mask_number):
    return '7000 79** **** 6361'


@pytest.fixture
def account(mask_account):
    return '**4305'


@pytest.fixture
def nums(mask_nums):
    return 'Счет **4305', 'Visa Platinum 7000 79** **** 6361', 'Maestro 7000 79** **** 6361'

@pytest.fixture
def data(date):
    return '26.07.2024'
