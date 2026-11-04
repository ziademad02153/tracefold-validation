from checkout.pricing import price_after_discount
from checkout.validation import is_valid_percent
def test_zero_discount(): assert price_after_discount(10000, 0) == 10000
def test_valid_percent(): assert is_valid_percent(20) is True
