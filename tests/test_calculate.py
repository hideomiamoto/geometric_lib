import unittest
from calculate import calc
from math import pi


class TestCalculate(unittest.TestCase):
    def test_valid_cases(self):
        test_cases = [
            ("circle", "area", [1], pi),
            ("circle", "perimeter", [1], 2 * pi),
            ("square", "area", [4], 16),
            ("square", "perimeter", [1], 4),
            ("triangle", "area", [6, 9], 27),
            ("triangle", "perimeter", [6, 8, 10], 24),
        ]

        for fig, func, size, expected in test_cases:
            with self.subTest(fig=fig, func=func, size=size):
                self.assertEqual(calc(fig, func, size), expected)

    def test_invalid_cases(self):
        test_cases = [
            ("rectangle", "area", [1]),  # Wrong figure
            ("circle", "angle", [1]),  # Wrong function
            ("square", "area", [1, 2]),  # Wrong size for square
            ("square", "area", [-1]),  # Negative size for square
            ("circle", "area", [-1]),  # Negative size for circle
            ("triangle", "area", [-6, -8, -10]),  # Negative size for triangle
            ("triangle", "area", [1, 2, 10]),  # Invalid triangle sides
        ]

        for fig, func, size in test_cases:
            with self.subTest(fig=fig, func=func, size=size):
                with self.assertRaises(AssertionError):
                    calc(fig, func, size)


if __name__ == "__main__":
    unittest.main()
