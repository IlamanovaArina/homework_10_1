def filter_by_currency(list_transactions, currency):
    """Фильтрует банковские операции по заданной валюте"""
    if len(list_transactions) > 0:
        filtered_transactions = filter(
            lambda list_transactions: list_transactions.get("operationAmount")
            .get("currency")
            .get("code")
            == currency,
            list_transactions,
        )
        return filtered_transactions
    else:
        return "Список пустой"


def transaction_descriptions(list_transactions):
    """Выводит операции по карте"""
    if len(list_transactions) > 0:
        for transaction in list_transactions:
            yield transaction.get("description")
    else:
        yield "Список пустой"


def card_number_generator(start: int, stop: int):
    """Функция может сгенерировать номера карт в заданном диапазоне
    от 0000 0000 0000 0001 до 9999 9999 9999 9999"""
    for x in range(start, stop + 1):
        number_zero = "0000000000000000"
        card_number = number_zero[: -len(str(x))] + str(x)
        yield (f"{card_number[:4]} {card_number[4:8]} "
               f"{card_number[8:12]} {card_number[12:]}")
