import json
import logging

logg_json_file = logging.getLogger("add.json_file")


def change_json_file(file_path: str) -> list:
    """Функция, которая принимает на вход путь до JSON-файла и
    возвращает список словарей с данными о финансовых транзакциях
    """
    if not file_path:
        logg_json_file.info("Файл пустой")
        return []
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            logg_json_file.info(f"Открыли файл: {file_path}")
            data: list = json.load(file)
            if type(data) is not list:
                logg_json_file.error("Не тот формат данных")
                return []
            logg_json_file.info("Возвращаю объект Python из Json файла")
            return data
    except FileNotFoundError:
        logg_json_file.error(f"Возникла ошибка: {FileNotFoundError}")
    except PermissionError:
        logg_json_file.error(f"Возникла ошибка: {PermissionError}")
    except Exception as e:
        logg_json_file.error(f"Возникла ошибка: {e}")
