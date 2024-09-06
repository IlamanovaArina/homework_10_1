from typing import Union

def mask_account_card(bank_card: Union[str]) -> Union[str]:
    """
    Функция которая принимает данные карты или счёта
    использует импортируемую функцию
    и возвращает в виде строки тип карты или счёта и
    маскированный номер карты/счёта
    """
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    account_or_number = []
    list_characters:Union[list] = []

    for symbol in bank_card:  # Перебераем каждый символ
        if symbol in numbers:
            list_characters += symbol  # Складываем цифы
        else:
            account_or_number.append(symbol)  # Складываем буквы

    type_card_or_account = "".join(account_or_number)  # Собираем слово

    if type_card_or_account != "Счет ":
        # Маскирует полученный номер карты
        mask_card = get_mask_card_number("".join(list_characters))
        return type_card_or_account + mask_card
    elif type_card_or_account == "Счет ":
        # Маскируем полученный "Счёт"
        mask_card = get_mask_account("".join(list_characters))
        return type_card_or_account + mask_card


def get_date(dat):
    """
    Функция возвращающая "ДД.ММ.ГГГГ" из строки
    такого образца"2024-03-11T02:26:18.671407"
    """
    return f"{dat[8:10]}.{dat[5:7]}.{dat[0:4]} "

