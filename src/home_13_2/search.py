import re
from collections import namedtuple


def search_for_transaction_data(transaction_data: list, search: str) -> list:
    """Функция, принимает список словарей
    с данными о банковских операциях и строку поиска,
    а возвращать список словарей, у которых в описании есть данная строка.
    """
    try:
        result = []
        pattern = re.compile(search, re.IGNORECASE)

        for transaction in transaction_data:
            if re.search(pattern, transaction["description"]):
                result.append(transaction)

            else:
                return result
        return result
    except Exception as e:
        print(f"Ошибка {e}")


def search_by_category(transactions: list, categories: list) -> dict:
    """Функция, принимает список словарей
    с данными о банковских операциях, список категорий операций,
    а возвращать словарь, в котором ключи — это названия категорий,
    а значения — это количество операций в каждой категории.
    Категории операций хранятся в поле description
    """
    try:
        Point = namedtuple('Point', ['description', 'operations'])
        description = []
        for transaction in transactions:
            if transaction.get("description") in categories:
                description.append(transaction.get("description"))

        number_operations = len(description)
        data_banking_transactions = Point(description, number_operations)
        return data_banking_transactions._asdict()
    except Exception as e:
        print(f"Ошибка {e}")
        return {}


# transaction_ = [{
#     "id": 939719570,
#     "state": "EXECUTED",
#     "date": "2018-06-30T02:08:58.425572",
#     "operationAmount": {
#         "amount": "9824.07",
#         "currency": {"name": "USD", "code": "USD"},
#     },
#     "description": "Перевод организации",
#     "from": "Счет 75106830613657916952",
#     "to": "Счет 11776614605963066702",
# },
#     {
#         "id": 939719571,
#         "state": "EXECUTED",
#         "date": "2019-06-30T02:08:58.425573",
#         "operationAmount": {
#             "amount": "9824.07",
#             "currency": {"name": "USD", "code": "USD"},
#         },
#         "description": "Перевод организации",
#         "from": "Счет 75106830613657916953",
#         "to": "Счет 11776614605963066703"
#     }]
#
# dikt = ["Перевод организации", "Перевод ЮР-лицу", "Покупка"]
#
#
# if __name__ == '__main__':
#     print(search_for_transaction_data(transaction_, "перевод"))
#     print(search_by_category(transaction_, dikt))
