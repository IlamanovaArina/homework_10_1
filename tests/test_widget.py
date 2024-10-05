import pytest

from src.Home_9_2.widget import get_date, mask_account_card


def test_widget_mask_account_card():
    assert (
        mask_account_card("Visa Platinum 7000792289606361")
        == "Visa Platinum 7000 79** **** 6361"
    )
    assert mask_account_card("Счет 73654108430135874305") == "Счет **4305"
    assert mask_account_card(700079223) == ""
    assert mask_account_card([]) == ""
    assert mask_account_card({}) == ""
    # assert mask_account_card("а если буквы, символы?") == ""
    # assert mask_account_card("а если 1 -буквы, 2 -символы и 3 -цыфры?") == ""
    with pytest.raises(TypeError):
        assert mask_account_card([7, 0, 0, 0, 7, 9, 2, 2, 3]) == "7000 79** *"
        assert mask_account_card() == ""


def test_widget_get_date():
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"
    assert get_date("") == ""
    assert get_date("11-03-2024") == "11.03.2024"
    with pytest.raises(TypeError):
        assert mask_account_card() == ""
