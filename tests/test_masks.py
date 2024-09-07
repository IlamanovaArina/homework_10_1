from src.Home_9_1.masks import get_mask_card_number, get_mask_account
import pytest

def test_masks():
    assert get_mask_card_number("7000792289606361") == "7000 79** **** 6361"
    assert get_mask_card_number("7000") == "7000"
    assert get_mask_card_number("7000123456789123456789") == "7000 12** **** 9123 4567 89"
    assert get_mask_card_number("пробуем буквы") == ""
    assert get_mask_card_number("") == ""
    assert get_mask_card_number(7000792289606361) == ""
    with pytest.raises(TypeError):
        assert get_mask_card_number() == ""


    assert get_mask_account("73654108430135874305") == "**4305"
    assert get_mask_account("7000792289606361") == "Ошибка"
    assert get_mask_account("7000") == "Ошибка"
    assert get_mask_account("7000123456789123456789") == "**6789"
    assert get_mask_account("пробуем буквы, очень много букв") == "Ошибка"
    assert get_mask_account("") == "Ошибка"
    assert get_mask_account(7000792289606361) == "Ошибка"
    with pytest.raises(TypeError):
        assert get_mask_account() == "Ошибка"
    assert get_mask_account("") == "Ошибка"