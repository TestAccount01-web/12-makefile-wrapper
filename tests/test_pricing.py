import pytest

from app.pricing import cart_total, divide


def test_cart_total(sample_items):
    assert cart_total(sample_items) == 25.5


def test_divide_returns_quotient_of_two_numbers():
    assert divide(10, 4) == 2.5


def test_divide_raises_zero_division_error_when_divisor_is_zero():
    with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
        divide(10, 0)
