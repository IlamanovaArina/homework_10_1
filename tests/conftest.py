import pytest

from tests.test_masks import test_masks
from tests.test_widget import (test_widget_get_date,
                               test_widget_mask_account_card)


@pytest.fixture
def bank_card():
    return test_widget_mask_account_card


@pytest.fixture
def dat():
    return test_widget_get_date


@pytest.fixture
def card_number():
    return test_masks
