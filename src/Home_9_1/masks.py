from typing import Union

def get_mask_card_number(card_number: Union[str]) -> Union[str]:
    """
    Функция которая принимает номер карты в виде целого числа
    и возвращяет маскированный номер кары
    """
    list_digit: Union[list] = []

    for key, value in enumerate(card_number):
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

    for digit in card_number:
        list_digit += digit
    list_digit[:-4] = '**'

    bank_card_str = "".join(list_digit)
    return bank_card_str
