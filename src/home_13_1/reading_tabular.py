import csv
import logging

import pandas as pd

logger_csv = logging.getLogger("transaction_csv.log")
logger_excel = logging.getLogger("transaction_excel.log")
logger_csv.setLevel(logging.DEBUG)
logger_excel.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename=r"C:\Users\minac.DESKTOP-L51PJSH\PycharmProjects"
                              r"\homework_10_1\src\home_13_1\logs.log",
                              encoding='utf-8')
formatter = logging.Formatter('%(asctime)s %(filename)s'
                              '%(funcName)s %(levelname)s - %(message)s')
handler.setFormatter(formatter)

logger_csv.addHandler(handler)
logger_excel.addHandler(handler)


file_path_csv_ = (r"C:\Users\minac.DESKTOP-L51PJSH\PycharmProjects"
                  r"\homework_10_1\data\transactions.csv")
file_path_xlsx_ = (r"C:\Users\minac.DESKTOP-L51PJSH\PycharmProjects"
                   r"\homework_10_1\data\transactions_excel.xlsx")

def reading_tables_csv(file_path_csv) -> list:
    """Функция которая открывает и читает файлы .csv
    возвращает список словарей
    """
    try:
        list_row = []
        with open(file_path_csv, encoding="utf-8") as csv_file:
            logger_csv.info(f"Открыт файл: {file_path_csv}")
            reader = csv.DictReader(csv_file, delimiter=';')
            for row in reader:
                list_row.append(row)

        return list_row

    except TypeError as t:
        logger_csv.error(f"Ошибка: {t}")
    except FileNotFoundError as f:
        logger_csv.error(f"Ошибка: {f}")
    except Exception as e:
        logger_csv.error(f"Ошибка: {e}")


def reading_tables_xlsx(file_path_xlsx) -> list:
    """Чтение Excel файла и вывод как список словарей"""
    try:
        df = pd.read_excel(file_path_xlsx)

        logger_excel.info(f"Открыли файл{file_path_xlsx}")

        transaction_excel = df.to_dict(orient='records')

        logger_excel.debug("Преобразовали данные из Exsel в список словарей")

        return transaction_excel

    except TypeError as t:
        logger_excel.error(f"Ошибка: {t}")
    except FileNotFoundError as f:
        logger_excel.error(f"Ошибка: {f}")
    except Exception as e:
        logger_excel.error(f"Ошибка: {e}")
