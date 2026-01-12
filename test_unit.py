import pytest
from banking import deposit, withdraw, calculate_interest, check_loan_eligibility


# ---------------- deposit ----------------
def test_deposit_valid():
    assert deposit(1000, 500) == 1500


def test_deposit_boundary():
    assert deposit(0, 1) == 1


def test_deposit_invalid():
    with pytest.raises(ValueError):
        deposit(1000, 0)


# ---------------- withdraw ----------------
def test_withdraw_valid():
    assert withdraw(1000, 300) == 700


def test_withdraw_boundary():
    assert withdraw(500, 500) == 0


def test_withdraw_insufficient():
    with pytest.raises(ValueError):
        withdraw(200, 300)


def test_withdraw_invalid():
    with pytest.raises(ValueError):
        withdraw(500, -10)


# ---------------- calculate_interest ----------------
def test_calculate_interest_valid():
    result = calculate_interest(1000, 10, 2)
    assert result == pytest.approx(1210.0)


def test_calculate_interest_boundary():
    assert calculate_interest(0, 5, 1) == 0


def test_calculate_interest_invalid_balance():
    with pytest.raises(ValueError):
        calculate_interest(-100, 5, 2)


def test_calculate_interest_invalid_rate():
    with pytest.raises(ValueError):
        calculate_interest(1000, -5, 2)


# ---------------- check_loan_eligibility ----------------
def test_loan_eligible():
    assert check_loan_eligibility(6000, 750) is True


def test_loan_not_eligible():
    assert check_loan_eligibility(3000, 650) is False


def test_loan_invalid_balance():
    with pytest.raises(ValueError):
        check_loan_eligibility(-500, 700)
