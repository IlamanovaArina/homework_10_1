import os
from unittest.mock import Mock, patch

from dotenv import load_dotenv

from src.home_12_1.external_api import transaction_amount

load_dotenv()
API_KEY = os.getenv("API_key")


@patch("requests.get")
def test_transaction_amount(mocked_get):
    mocked_response_usd = Mock()
    mocked_response_usd.ok = True
    mocked_response_usd.text = '{"result": 3341.74}'
    mocked_get.return_value = mocked_response_usd

    transaction_data_usd = [
        {"operationAmount": {"currency": {"code": "USD"}, "amount": 36}}
    ]

    assert transaction_amount(transaction_data_usd) == 3341.74

    mocked_get.assert_called_once_with(
        "https://api.apilayer.com/currency_data/convert",
        params={"amount": 36, "from": "USD", "to": "RUB", "apikey": API_KEY},
    )

    mocked_response_eur = Mock()
    mocked_response_eur.ok = True
    mocked_response_eur.text = '{"result": 3716.56}'
    mocked_get.return_value = mocked_response_eur

    transaction_data_eur = [
        {"operationAmount": {"currency": {"code": "EUR"}, "amount": 36}}
    ]

    assert transaction_amount(transaction_data_eur) == 3716.56

    mocked_response_rub = Mock()
    mocked_response_rub.ok = True
    mocked_response_rub.text = '{"result": 36}'
    mocked_get.return_value = mocked_response_rub

    transaction_data_rub = [
        {"operationAmount": {"currency": {"code": "EUR"}, "amount": 36}}
    ]

    assert transaction_amount(transaction_data_rub) == 36
