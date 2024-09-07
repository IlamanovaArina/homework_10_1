from typing import Union

from src.data import acceptable_data, numbers
from src.Home_9_1.masks import get_mask_account, get_mask_card_number


def mask_account_card(bank_card: str) -> str:
    """
    Функция которая принимает данные карты или счёта
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

    if type_card_or_account in acceptable_data:
        if type_card_or_account != "Счет":
            # Маскирует полученный номер карты
            mask_card = get_mask_card_number("".join(list_characters))
            return type_card_or_account + " " + mask_card
        elif type_card_or_account == "Счет":
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
