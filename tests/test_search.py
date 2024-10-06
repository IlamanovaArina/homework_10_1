from src.home_13_2.search import (search_by_category,
                                  search_for_transaction_data)


def test_search_for_transaction_data(list_transactions):
    assert search_for_transaction_data(list_transactions, "перевод") == [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 939719571,
            "state": "EXECUTED",
            "date": "2019-06-30T02:08:58.425573",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916953",
            "to": "Счет 11776614605963066703",
        },
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 939719571,
            "state": "EXECUTED",
            "date": "2019-06-30T02:08:58.425573",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916953",
            "to": "Счет 11776614605963066703",
        },
    ]


def test_search_by_category(list_transactions):
    dikt = ["Перевод организации", "Перевод ЮР-лицу", "Покупка"]

    assert search_by_category(list_transactions, dikt)
