import json


def change_json_file(file_path: str) -> list:
    """
    Функция, которая принимает на вход путь до JSON-файла и
    возвращает список словарей с данными о финансовых транзакциях
    """
    if not file_path:
        return []
    try:
        with open(file_path, "r", encoding="utf-8", errors="replace") as file:
            data: list = json.load(file)
            if type(data) != list:
                return []
            return data
    except FileNotFoundError:
        return []
    except PermissionError:
        print("В доступе отказано")
