import unittest
from service import price_after_discount, run_with_retries


class BehaviorTests(unittest.TestCase):
    def test_discount_reduces_price(self):
        self.assertEqual(price_after_discount(10000, 20), 8000)

    def test_discount_boundaries(self):
        self.assertEqual(price_after_discount(10000, 0), 10000)
        self.assertEqual(price_after_discount(10000, 100), 0)

    def test_successful_operation_is_called_once(self):
        calls = []
        result = run_with_retries(lambda: calls.append(1) or "ok", 3)
        self.assertEqual(result, "ok")
        self.assertEqual(len(calls), 1)

    def test_retry_limit_counts_total_attempts(self):
        calls = []
        def fail():
            calls.append(1)
            raise ValueError("Temporary failure")
        with self.assertRaises(ValueError):
            run_with_retries(fail, 3)
        self.assertEqual(len(calls), 3)


if __name__ == "__main__":
    unittest.main(verbosity=2)
