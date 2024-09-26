import pytest

from src.Home_9_1.masks import get_mask_account, get_mask_card_number


def test_masks():
    assert get_mask_card_number("7000792289606361") == "7000 79** **** 6361"
    assert get_mask_card_number("7000") == "7000"
    assert (get_mask_card_number("7000123456789123456") ==
            "7000 12** **** 9123 456")
    assert get_mask_card_number("пробуем буквы") == ""
    assert get_mask_card_number("") == ""
    assert get_mask_card_number(7000792289606361) == ""
    with pytest.raises(TypeError):
        assert get_mask_card_number() == ""

    assert get_mask_account("73654108430135874305") == "**4305"
    assert get_mask_account("7000792289606361") == "Недостаточно цифр"
    assert get_mask_account("7000") == "Недостаточно цифр"
    assert get_mask_account("7000123456789123456789") == "Недостаточно цифр"
    # assert get_mask_account("пробуем буквы, очень много букв") == "Недостаточно цифр"
    assert get_mask_account("") == "Недостаточно цифр"
    assert get_mask_account(7000792289606361) == "Недостаточно цифр"
    with pytest.raises(TypeError):
        assert get_mask_account() == "Недостаточно цифр"
    assert get_mask_account("") == "Недостаточно цифр"
