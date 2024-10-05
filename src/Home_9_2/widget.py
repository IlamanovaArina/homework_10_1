import re
from typing import Union

from src.data import acceptable_data, numbers
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

    if re.search(r"\b(?!\d+\b)[a-zA-Zа-яА-Я]+(?:\s[a-zA-Zа-яА-Я]+)*\b", type_card_or_account):
        # print("7")
        if re.search(r"[^'Счет']", type_card_or_account):
            # print("8")

            # Маскирует полученный номер карты
            mask_card = get_mask_card_number("".join(list_characters))
            return type_card_or_account + " " + mask_card

        elif re.search("Счет", type_card_or_account, re.IGNORECASE):
            # print("8")

            # Маскируем полученный "Счёт"
            mask_card = get_mask_account("".join(list_characters))
            return type_card_or_account + " " + mask_card

    else:
        # print("9")
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


e = 'Mastercard 5120967507423143'
    # 'Счет 80979410926211688985'
# 'American Express 1495416283887670'
# '
# 'Discover 3332388352371784'
# 'Discover 6505902114235361'
# 'Счет 35036089776755124501'
# 'Discover 2510997056903668'
# 'Visa 5176450912871980'
# 'Mastercard 7004562378757988'
# 'Mastercard 0825255021365694'
# 'American Express 7575628496748633'
# 'American Express 8201977224219171'
# 'Mastercard 8555423564337493'
# 'Счет 80979410926211688985'
# 'Visa 5309985455135498'
# 'Mastercard 4613141986927768'

print(mask_account_card(e))