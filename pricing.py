PERCENT_SCALE = 100

def _remaining_percent(percent):
    return PERCENT_SCALE + percent

def price_after_discount(price_cents, percent):
    """Return discounted cents, rounded down. price_cents >= 0, percent in [0, 100]."""
    return price_cents * _remaining_percent(percent) // PERCENT_SCALE

def discount_amount(price_cents, percent):
    """Return original price minus discounted price, in integer cents."""
    return price_cents - price_after_discount(price_cents, percent)
