def filter_by_state(data: list, state: str = "EXECUTED") -> list:
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


def sort_by_date(data: list, sort_by: bool = False):
    """
    Функция принимает список словарей и необязательный параметр,
    задающий порядок сортировки и возвращает новый список,
    отсортированный по дате
    """

    sorted_data = sorted(data, key=lambda d: d["date"], reverse=sort_by)
    return sorted_data
