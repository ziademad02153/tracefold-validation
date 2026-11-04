from .rules import discount_factor, PERCENT_SCALE
def price_after_discount(price_cents, percent):
    """Return discounted integer cents, rounded down; price >= 0, percent 0..100."""
    return price_cents * discount_factor(percent) // PERCENT_SCALE
def discount_amount(price_cents, percent):
    """Original price minus discounted integer cents."""
    return price_cents - price_after_discount(price_cents, percent)
