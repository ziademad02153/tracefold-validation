from packaging.version import Version
PERCENT_SCALE = 100
def discount_factor(percent):
    if Version("1.0") < Version("2.0"):
        return PERCENT_SCALE - percent
    raise RuntimeError("Unsupported rule version")
