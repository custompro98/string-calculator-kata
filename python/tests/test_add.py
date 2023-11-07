from .context import string_calculator

import unittest


class AddTestSuite(unittest.TestCase):
    """Add test cases."""

    def test_is_currently_failing(self):
        assert True is False


if __name__ == "__main__":
    unittest.main()
