from typing import Union

from src.data import numbers


def get_mask_card_number(card_number: Union[str]) -> Union[str]:
    """
    Функция которая принимает номер карты в виде целого числа
    и возвращяет маскированный номер кары
    """
    list_digit: Union[list] = []

    if type(card_number) is not str or type(card_number) is bool:
        return ""

    for key, value in enumerate(card_number):
        if value not in numbers:
            return ""
        if key % 4 == 0 and key != 0:
            list_digit.append(" ")
        if len(list_digit) <= 6 or len(list_digit) > 13:
            list_digit += value
        elif len(list_digit) > 6 or len(list_digit) < 12:
            list_digit += "*"
        else:
            return "Что-то пошло не так ;)"

    bank_card_str = "".join(list_digit)
    return bank_card_str


def get_mask_account(card_number: Union[str]) -> Union[str]:
    """
    Функция которая принимает номер каты
    и возвращает маску ввиде две '*' и 4 цифры
    """
    list_digit: Union[list] = []
    intake = ""

    if type(card_number) is not int:
        if len(card_number) < 20:
            return "Ошибка"
    if type(card_number) is not str or type(card_number) is bool:
        return "Ошибка"

    for digit in card_number:
        if digit in numbers:
            list_digit += digit
            intake = "yes"

    if intake == "yes":
        list_digit[:-4] = "**"
    else:
        return "Ошибка"

    bank_card_str = "".join(list_digit)
    return bank_card_str
