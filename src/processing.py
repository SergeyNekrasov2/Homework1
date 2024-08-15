list_of_dicts = [
    [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
     {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
     {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
     {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
]


def filter_by_state(list_of_dicts: list[dict[str]], state_id="EXECUTED") -> list[dict[str]]:
    """
        Функция принимает на вход список словарей и значение для ключа и возвращает новый
        список содержащий только те словари у которых ключ содержит переданное в функцию
        значение.
        """
    list_state = []

    for key in list_of_dicts:
        if key.get("state") == state_id:
            list_state.append(key)

    return list_state


def sort_by_date(list_of_dicts: list[dict[str]], reverse=True) -> list[dict[str]]:
    """Функция сортирующая исходные данные по дате"""
    sorted_list_of_dicts = sorted(list_of_dicts, key=lambda list_of_dicts: list_of_dicts['date'], reverse=reverse)

