import re
from typing import Union

from src.data import numbers
from src.Home_9_1.masks import get_mask_account, get_mask_card_number


def mask_account_card(bank_card: str) -> str:
    """
    Функция принимает данные карты или счёта
    использует импортируемую функцию
    и возвращает в виде строки тип карты или счёта и
    маскированный номер карты/счёта
    """
    account_or_number = []
    list_characters: Union[list] = []
    entered_data = []

    if not hasattr(bank_card, "__iter__"):
        return ""
    if bank_card == [] or bank_card == {} or bank_card == ():
        return ""

    for symbols in bank_card:
        entered_data.append(symbols)

    entered_data_str = "".join(entered_data)

    for symbol in entered_data_str:  # Перебераем каждый символ
        if symbol in numbers:
            list_characters += symbol  # Складываем цифы
        else:
            account_or_number.append(symbol)  # Складываем буквы

    type_card_or_account = "".join(account_or_number[:-1])  # Собираем слово

    # print(type_card_or_account)
    # print(account_or_number)
    # print(list_characters)
    # print(entered_data)

    regular_expression = r"\b(?!\d+\b)[a-zA-Zа-яА-Я]+(?:\s[a-zA-Zа-яА-Я]+)*\b"

    if re.search(regular_expression, type_card_or_account):
        if re.search(r"[^'Счет']", type_card_or_account):

            # Маскирует полученный номер карты
            mask_card = get_mask_card_number("".join(list_characters))
            return type_card_or_account + " " + mask_card

        elif re.search("Счет", type_card_or_account, re.IGNORECASE):

            # Маскируем полученный "Счёт"
            mask_card = get_mask_account("".join(list_characters))
            return type_card_or_account + " " + mask_card

    else:
        return ""


def get_date(dat: str) -> str:
    """
    Функция возвращающая "ДД.ММ.ГГГГ" из строки
    такого образца "2024-03-11T02:26:18.671407"
    """
    if dat == "":
        return ""

    if "T" in dat:
        string = "".join(dat.split("T")[0])
        year, month, day = string.split("-")
        return f"{day}.{month}.{year}"
    else:
        a, month, c = dat.split("-")
        len_a = len(a)
        len_c = len(c)

        if len_a == 4:
            return f"{c}.{month}.{a}"
        elif len_c == 4:
            return f"{a}.{month}.{c}"
