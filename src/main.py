import os


def main(file):
    """Функция, которая отвечает за основную логику проекта
    и связывает функциональности между собой
    """
    try:

        list_data = []

        print(
            "Привет! Добро пожаловать в программу работы с "
            "банковскими транзакциями.\n"
            "Выберите необходимый пункт меню:\n"
            "1. Получить информацию о транзакциях из JSON-файла\n"
            "2. Получить информацию о транзакциях из CSV-файла\n"
            "3. Получить информацию о транзакциях из XLSX-файла"
        )

        file_type = {"1": "JSON-файл", "2": "CSV-файл", "3": "XLSX-файл"}

        # пользователь выбирает с каким файлом работать
        file_selection: str = input().lower()

        if str(file_selection) in file_type:

            print(f"Для обработки выбран {file_type.get(file_selection)}")

            if file.endswith(".json"):
                from src.home_12_1.utils import change_json_file

                # Вызываю функцию для открытья JSON-файл
                list_data = change_json_file(file)

            elif file.endswith(".csv"):
                from src.home_13_1.reading_tabular import (
                    reading_tables_csv,
                    converting_template,
                )

                # Вызываю функцию для открытья CSV-файл
                list_data = converting_template(reading_tables_csv(file))

            elif file.endswith(".xlsx"):
                from src.home_13_1.reading_tabular import (
                    reading_tables_xlsx,
                    converting_template,
                )

                # Вызываю функцию для открытья XLSX-файл
                list_data = converting_template(reading_tables_xlsx(file))

        else:
            print(
                "Такой программы не найдено.\n"
                "Выберите необходимый пункт меню:\n"
                "1. Получить информацию о транзакциях из JSON-файла\n"
                "2. Получить информацию о транзакциях из CSV-файла\n"
                "3. Получить информацию о транзакциях из XLSX-файла"
            )

        print(
            "Введите статус, по которому необходимо выполнить фильтрацию.\n"
            "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"
        )

        sorting_method = ["EXECUTED", "CANCELED", "PENDING"]
        choice = input().upper()  # выбор пользователя для фильтрации

        if choice in sorting_method:
            from src.home_10_1.processing import filter_by_state

            # Вызываю функцию для фильтрации по sorting_method
            list_data = filter_by_state(list_data, choice)

            print(f"Операции отфильтрованы по статусу {choice}")

        else:
            print(f"Статус операции {choice} недоступен.")

        print("Отсортировать операции по дате? Да/Нет")
        user_response = input().lower()

        if user_response.lower() == "да":

            print("Отсортировать по возрастанию или по убыванию?")

            sorting_response = input().lower()

            if sorting_response.lower() in "убыванию":
                from src.home_10_1.processing import sort_by_date

                # Вызываем функцию для сортировки по убыванию
                list_data = sort_by_date(list_data, sort_by=True)

            elif sorting_response.lower() in "возрастанию":
                from src.home_10_1.processing import sort_by_date

                # Вызываем функцию для сортировки по возрастанию
                list_data = sort_by_date(list_data)

            else:
                print("Ошибка, попробуйте ещё раз")

        print("Выводить только рублевые тразакции? Да/Нет")
        answer_currency = input().lower()

        if answer_currency == "да":
            from src.home_11_1.generators import filter_by_currency

            #
            list_data = filter_by_currency(list_data, "RUB")

        print(
            "Отфильтровать список транзакций по " "определенному слову в описании? Да/Нет"
        )

        answer_search_word = input().lower()

        if answer_search_word == "да":
            from src.home_13_2.search import search_for_transaction_data

            print("Введите слово:\n")
            search = input().lower()

            #
            list_data = search_for_transaction_data(list_data, search)

        print("Распечатываю итоговый список транзакций...\n")
        if len(list_data) == 0:
            return "Не найдено ни одной транзакции, подходящей под ваши условия фильтрации"

        else:

            print(f"Всего банковских операций в выборке: {len(list_data)}\n")

        from src.Home_9_2.widget import get_date, mask_account_card

        for transaction in list_data:

            # получаю дату нужного формата
            data = get_date(transaction["date"])


            if transaction["from"]:
                mask_from = mask_account_card(transaction["from"])
                mask_to = mask_account_card(transaction["to"])

                print(
                    f"\n{data} {transaction['description']}\n"
                    f"{mask_from} -> "
                    f"{mask_to}\n"
                    f"Сумма: {transaction["operationAmount"]["amount"]} "
                    f"{transaction["operationAmount"]["currency"]["code"]}"
                )
            else:
                mask_to = mask_account_card(transaction["to"])

                print(
                    f"\n{data} {transaction['description']}\n"
                    f"{mask_to}\n"
                    f"Сумма: {transaction["operationAmount"]["amount"]} "
                    f"{transaction["operationAmount"]["currency"]["code"]}"
                )

    except Exception as er:
        return f"Ошибка {er}"


if __name__ == "__main__":
    e = r"C:\Users\minac.DESKTOP-L51PJSH\PycharmProjects\homework_10_1\data\operations.json"
    a = r"C:\Users\minac.DESKTOP-L51PJSH\PycharmProjects\homework_10_1"
    s = os.path.join(a, "data", "transactions_excel.xlsx")
    b = os.path.join(a, "data", "transactions.csv")
    print(main(s))
