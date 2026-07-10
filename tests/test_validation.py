import math
import unittest

from app.core.validation import ValidationError, validate_strictly_increasing


class ValidationTests(unittest.TestCase):
    def test_strictly_increasing_depth_passes(self):
        self.assertEqual(validate_strictly_increasing([0.0, 1.0, 2.0]), [0.0, 1.0, 2.0])

    def test_duplicate_depth_fails(self):
        with self.assertRaises(ValidationError):
            validate_strictly_increasing([0.0, 1.0, 1.0])

    def test_nan_depth_fails(self):
        with self.assertRaises(ValidationError):
            validate_strictly_increasing([0.0, math.nan, 2.0])


if __name__ == "__main__":
    unittest.main()

