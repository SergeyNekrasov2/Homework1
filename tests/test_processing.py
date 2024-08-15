# import pytest
#
# from src.processing import filter_by_state, sort_by_date
#
#
# @pytest.mark.parametrize("list_of_dicts, list_state", [
#     [({'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, True),
#      ({'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, True),
#      ({'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, False),
#      ({'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}, False)]
# ])
# def test_filter_by_state(state):
#     """Тест для функции которая принимает на вход список словарей и значение для ключа и возвращает новый
#         список содержащий только те словари у которых ключ содержит переданное в функцию
#         значение"""
#     assert filter_by_state(list_of_dicts) == 'list_state'
#     assert filter_by_state(list_of_dicts) == 'list_state'
#
#
# @pytest.mark.parametrize("dicts, sorted_dicts",[
#     [({'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, True),
#      ({'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, True),
#      ({'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, False),
#      ({'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}, False)]
# ])
# def test_sort_by_date(dicts, sorted_dicts):
#     """Тест для функции сортирующей исходные данные по дате"""
#     assert sort_by_date(dicts) == 'sorted_dicts'
#     assert sort_by_date(dicts) == 'sorted_dicts'

def test_filter_by_state(state):
    """Тест для функции которая принимает на вход список словарей и значение для ключа и возвращает новый
         список содержащий только те словари у которых ключ содержит переданное в функциюзначение"""
    assert filter_by_state(state) == [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                                      {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]


def test_filter_by_state_canceled(state):
    assert filter_by_state(state, 'CANCELED') == [
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]


def test_sort_by_date(state):
    """Тест для функции сортирующей исходные данные по дате"""
    assert sort_by_date(state, False) == [{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                                          {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                                          {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
                                          {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}]


def test_sort_by_date_reverse(state):
    assert sort_by_date(state, True) == [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                                         {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
                                         {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                                         {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
