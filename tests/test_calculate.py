import unittest
from calculate import calc
from math import pi


class TestCalculate(unittest.TestCase):
    def test_valid_cases(self):
        test_cases = [
            ("circle", "area", [1], pi),
            ("square", "area", [4], 16),
            ("triangle", "area", [6, 9], 27),
            ("circle", "perimeter", [1], 2 * pi),
            ("square", "perimeter", [1], 4),
            ("triangle", "perimeter", [5, 12, 13], 30),
        ]

        for fig, func, size, expected in test_cases:
            with self.subTest(fig=fig, func=func, size=size):
                self.assertEqual(calc(fig, func, size), expected)

    def test_invalid_cases(self):
        test_cases = [
            ("rectangle", "area", [1]),  # Wrong figure
            ("circle", "angle", [1]),  # Wrong function
            ("square", "area", [1, 2]),  # Wrong size for square
            ("circle", "area", [-1]),  # Negative size for circle
            ("square", "area", [-1]),  # Negative size for square
            ("triangle", "area", [-5, -12, -13]),  # Negative size for triangle
            ("triangle", "area", [1, 2, 10]),  # Invalid triangle sides
        ]

        for fig, func, size in test_cases:
            with self.subTest(fig=fig, func=func, size=size):
                with self.assertRaises(AssertionError):
                    calc(fig, func, size)

if __name__ == "__main__":
    unittest.main()