import json
import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_key')

def transaction_amount(transaction_data: list) -> float:
    """ Функцию, которая принимает на вход транзакцию и возвращает сумму транзакции в рублях """
    try:
        code = transaction_data[0].get("operationAmount").get("currency").get("code")
        amount = transaction_data[0].get("operationAmount").get("amount")
        if code == "RUB":
            return amount
        else:
            url = "https://api.apilayer.com/currency_data/convert"
            if code == 'USD':
                payload = {
                    "amount": amount,
                     "from": "USD",
                     "to": "RUB",
                     "apikey": API_KEY
                }
            elif code == 'EUR':
                payload = {
                    "amount": amount,
                    "from": "EUR",
                    "to": "RUB",
                    "apikey": API_KEY
                }
            response = requests.get(url, payload)
            if response.ok:
                obj = json.loads(response.text)
                amount = obj.get("result")
                return round(amount, 2)

    except Exception:
        print("Что-то пошло не так")
