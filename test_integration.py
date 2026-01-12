import pytest
from banking import transfer, calculate_interest


def test_transfer_success():
    balance_from, balance_to = transfer(1000, 500, 300)
    assert balance_from == 700
    assert balance_to == 800


def test_transfer_and_interest():
    balance_from, balance_to = transfer(2000, 1000, 500)
    updated_balance = calculate_interest(balance_to, 10, 1)
    assert updated_balance == pytest.approx(1650.0)


def test_transfer_insufficient_balance():
    with pytest.raises(ValueError):
        transfer(200, 500, 300)


def test_transfer_invalid_amount():
    with pytest.raises(ValueError):
        transfer(1000, 500, -50)
