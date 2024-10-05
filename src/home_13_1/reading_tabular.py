import csv
import logging

import pandas as pd

logger_csv = logging.getLogger("transaction_csv.log")
logger_excel = logging.getLogger("transaction_excel.log")
logger_csv.setLevel(logging.DEBUG)
logger_excel.setLevel(logging.DEBUG)
handler = logging.FileHandler(
    filename=r"C:\Users\minac.DESKTOP-L51PJSH\PycharmProjects"
             r"\homework_10_1\src\home_13_1\logs.log",
    encoding="utf-8",
)
formatter = logging.Formatter(
    "%(asctime)s %(filename)s" "%(funcName)s %(levelname)s - %(message)s"
)
handler.setFormatter(formatter)

logger_csv.addHandler(handler)
logger_excel.addHandler(handler)

file_path_csv_ = (
    r"C:\Users\minac.DESKTOP-L51PJSH\PycharmProjects"
    r"\homework_10_1\data\transactions.csv"
)
file_path_xlsx_ = (
    r"C:\Users\minac.DESKTOP-L51PJSH\PycharmProjects"
    r"\homework_10_1\data\transactions_excel.xlsx"
)


def reading_tables_csv(file_path_csv: str) -> list:
    """Функция открывает и читает файлы .csv,
    возвращает список словарей
    """
    try:
        list_row = []
        with open(file_path_csv, encoding="utf-8") as csv_file:
            logger_csv.info(f"Открыт файл: {file_path_csv}")
            reader = csv.DictReader(csv_file, delimiter=";")
            for row in reader:
                list_row.append(row)

        return list_row

    except TypeError as t:
        logger_csv.error(f"Ошибка: {t}")
    except FileNotFoundError as f:
        logger_csv.error(f"Ошибка: {f}")
    except Exception as e:
        logger_csv.error(f"Ошибка: {e}")


def reading_tables_xlsx(file_path_xlsx: str) -> list:
    """Чтение Excel файла и вывод как список словарей"""
    try:
        df = pd.read_excel(file_path_xlsx)

        logger_excel.info(f"Открыли файл{file_path_xlsx}")

        transaction_excel = df.to_dict(orient="records")

        logger_excel.debug("Преобразовали данные из Exsel в список словарей")

        return transaction_excel

    except TypeError as t:
        logger_excel.error(f"Ошибка: {t}")
    except FileNotFoundError as f:
        logger_excel.error(f"Ошибка: {f}")
    except Exception as e:
        logger_excel.error(f"Ошибка: {e}")


def converting_template(l_transactions: list) -> list:
    """Функция принимат данные из открытых файлов Exsel и csv
    и возвращает список нужной мне структуры"""
    transactions = []
    for dict_ in l_transactions:
        s = {
            "id": dict_["id"],
            "state": dict_["state"],
            "date": dict_["date"],
            "operationAmount": {
                "amount": dict_["amount"],
                "currency": {"name": dict_["currency_name"], "code": dict_["currency_code"]},
            },
            "description": dict_["description"],
            "from": dict_["from"],
            "to": dict_["to"],
        }
        transactions.append(s)
    return transactions


a = [{'id': '4361453', 'state': 'EXECUTED', 'date': '2021-12-05T01:35:38Z', 'amount': '30045',
      'currency_name': 'Yuan Renminbi', 'currency_code': 'CNY', 'from': 'Mastercard 3665700271480451',
      'to': 'American Express 0562165846839124', 'description': 'Перевод с карты на карту'},
     {'id': '413942', 'state': 'EXECUTED', 'date': '2023-01-14T17:09:31Z', 'amount': '30885', 'currency_name': 'Zloty',
      'currency_code': 'PLN', 'from': '', 'to': 'Счет 14333875659976842245', 'description': 'Открытие вклада'},
     {'id': '3034414', 'state': 'EXECUTED', 'date': '2020-05-17T04:31:24Z', 'amount': '14490',
      'currency_name': 'Rupiah', 'currency_code': 'IDR', 'from': 'Mastercard 5542284288235939',
      'to': 'Discover 6909942117751005', 'description': 'Перевод с карты на карту'},
     {'id': '595305', 'state': 'PENDING', 'date': '2023-08-22T17:20:18Z', 'amount': '22624', 'currency_name': 'Euro',
      'currency_code': 'EUR', 'from': '', 'to': 'Счет 97565556730475585217', 'description': 'Открытие вклада'},
     {'id': '2415946', 'state': 'EXECUTED', 'date': '2020-10-28T08:59:58Z', 'amount': '23190', 'currency_name': 'Kuna',
      'currency_code': 'HRK', 'from': 'Visa 2130676513423745', 'to': 'Счет 65656300853632903109',
      'description': 'Перевод организации'},
     {'id': '3330422', 'state': 'EXECUTED', 'date': '2023-08-05T07:11:26Z', 'amount': '30065', 'currency_name': 'Ruble',
      'currency_code': 'RUB', 'from': 'Mastercard 9458117363112215', 'to': 'Visa 6335859532296628',
      'description': 'Перевод с карты на карту'}
     ]
print(converting_template(a))
