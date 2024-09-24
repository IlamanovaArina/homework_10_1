import logging
from typing import Union

from src.data import numbers

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(filename)s %(funcName)s %(levelname)s - %(message)s",
    filename=r"C:\Users\minac.DESKTOP-L51PJSH\
    PycharmProjects\homework_10_1\logs.log",
    filemode="w",
    encoding="utf-8"
)

log_masks = logging.getLogger("add.masks")
log_mask_account = logging.getLogger("add.mask_account")


def get_mask_card_number(card_number: str) -> str:
    """Функция которая принимает номер карты в виде целого числа(str)
    и возвращяет маскированный номер кары(str)
    """
    list_digit: Union[list] = []

    if type(card_number) is not str or type(card_number) is bool:
        log_masks.info("Получили не тот тип данных.")
        return ""

    for key, value in enumerate(card_number):
        if value not in numbers:
            return ""
        if key % 4 == 0 and key != 0:
            log_masks.info("После 4-х цифр ставлю пробел")
            list_digit.append(" ")
        if len(list_digit) <= 6 or len(list_digit) > 13:
            log_masks.info("Добавляю в list_digit цифры номера карты")
            list_digit += value
        elif len(list_digit) > 6 or len(list_digit) < 12:
            log_masks.info("Меняю часть цифр на *")
            list_digit += "*"
        else:
            log_masks.warning("Введены не цифры")
            return "Что-то пошло не так ;)"

    bank_card_string = "".join(list_digit)
    return bank_card_string


def get_mask_account(card_number: Union[str]) -> Union[str]:
    """
    Функция которая принимает номер каты
    и возвращает маску ввиде две '*' и 4 цифры
    """
    list_digit: Union[list] = []
    try:
        if type(card_number) is not str or type(card_number) is bool:
            log_mask_account.info("Получили не тот тип данных.")
            return "Ошибка"

        for d in card_number:
            digit = int(d)
            if type(digit) is int:
                list_digit.append(digit)
        log_mask_account.info("Перебрали цифры, сложили в словарь")

        if len(list_digit) == 20:
            log_mask_account.info("Маскируем номер счёта")
            list_digit[:-4] = ['*', '*']
        else:
            log_mask_account.error("Ввели короткий номер счёта, "
                                   "недостаточно цифр")
            return "Недостаточно цифр"

        bank_card_string = "".join(map(str, list_digit))
        return bank_card_string

    except TypeError:
        log_mask_account.critical("Ввели не тот тип данных")
    except Exception as e:
        log_mask_account.critical(f"Возникла ошибка: {e}")
