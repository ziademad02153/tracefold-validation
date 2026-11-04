def price_after_discount(price_cents, percent):
    """Return discounted integer cents. Inputs: price_cents >= 0, 0 <= percent <= 100."""
    return price_cents * (100 - percent) // 100


def run_with_retries(operation, max_attempts):
    """Call operation at most max_attempts times. max_attempts is a positive integer."""
    for attempt in range(max_attempts):
        try:
            return operation()
        except ValueError:
            if attempt == max_attempts:
                raise
