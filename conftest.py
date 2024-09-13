import pytest

from tests.test_masks import test_masks
from tests.test_widget import test_widget_get_date, test_widget_mask_account_card
from tests.test_generators import test_filter_by_currency, test_transaction_descriptions


@pytest.fixture
def bank_card():
    return test_widget_mask_account_card


@pytest.fixture
def dat():
    return test_widget_get_date


@pytest.fixture
def card_number():
    return test_masks


@pytest.fixture
def list_transaction():
    return test_filter_by_currency


@pytest.fixture
def required_currency():
    return test_filter_by_currency


@pytest.fixture
def list_transactions():
    transaction = [
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
    }
    ]
    return transaction


@pytest.fixture
def start():
    return "0000 0000 0000 0001"


@pytest.fixture
def stop():
    return "9999 9999 9999 9999"