from src.home_12_1.utils import change_json_file


def test_utils(file_path_test):
    transaction = None
    assert change_json_file(file_path_test) == [
        {
            "id": 667307132,
            "state": "EXECUTED",
            "date": "2019-07-13T18:51:29.313309",
            "operationAmount": {
                "amount": "97853.86",
                "currency": {"name": "руб.", "code": "RUB"},
            },
            "description": "Перевод с карты на счет",
            "from": "Maestro 1308795367077170",
            "to": "Счет 96527012349577388612",
        }
    ]
    assert change_json_file([]) == []
    assert change_json_file(transaction) == []
