from unittest.mock import patch

from src.home_12_1.external_api import transaction_amount


@patch("src.home_12_1.external_api.requests.get")
def test_transaction_amount(mock_get):
    mock_get.return_value.ok = True
    mock_get.return_value.texst = '{"result": 75.0}'

    assert (
        transaction_amount(
            [
                {
                    "id": 441945886,
                    "state": "EXECUTED",
                    "date": "2019-08-26T10:50:58.294041",
                    "operationAmount": {
                        "amount": "50.0",
                        "currency": {"name": "руб.", "code": "USD"},
                    },
                    "description": "Перевод организации",
                    "from": "Maestro 1596837868705199",
                    "to": "Счет 64686473678894779589",
                }
            ]
        )
        == 75.0
    )

    mock_get.assert_called_once()
