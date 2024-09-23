import json
import os

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_key")


def transaction_amount(transaction_data: list) -> float:
    """
    Функцию, которая принимает на вход транзакцию и
    возвращает сумму транзакции в рублях
    """
    try:
        code = (transaction_data[0].get("operationAmount")
                .get("currency").get("code"))
        amount = transaction_data[0].get("operationAmount").get("amount")
        if code == "RUB":
            return amount
        else:
            url = "https://api.apilayer.com/currency_data/convert"
            if code == "USD" or code == "EUR":
                payload = {
                    "amount": amount,
                    "from": code,
                    "to": "RUB",
                    "apikey": API_KEY,
                }

            response = requests.get(url, params=payload)
            print(response.text)
            if response.ok:
                obj = json.loads(response.text)
                amount = obj.get("result")
                return round(amount, 2)

    except KeyError:
        print("Ошибка поиска по ключу")

    return 0  # Возвращаем значение по умолчанию


a = [
    {
        "id": 667307132,
        "state": "EXECUTED",
        "date": "2019-07-13T18:51:29.313309",
        "operationAmount": {
            "amount": "97853.86",
            "currency": {"name": "руб.", "code": "EUR"},
        },
        "description": "Перевод с карты на счет",
        "from": "Maestro 1308795367077170",
        "to": "Счет 96527012349577388612",
    }
]

print(transaction_amount(a))
