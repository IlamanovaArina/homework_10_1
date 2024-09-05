from tests.test_processing import true_or_false, user_state, user_data


def filter_by_state(data: list, state="EXECUTED") -> list:
    """
    Функция принимает список словарей и возвращает новый список словарей,
    содержащий только те словари, у которых ключь 'state'
    соответствует указанному значению.
    """
    new_data: list = []

    for dict_data in data:
        if dict_data.get("state") == state:
            new_data.append(dict_data)

    return new_data


def sort_by_date(data: list, sort_by=true_or_false):
    """
    Функция принимает список словарей и необязательный параметр,
    задающий порядок сортировки и возвращает новый список,
    отсортированный по дате
    """

    sorted_data = sorted(data, key=lambda d: d["date"], reverse=sort_by)
    return sorted_data


print(filter_by_state(user_data, user_state))
print(sort_by_date(user_data))
