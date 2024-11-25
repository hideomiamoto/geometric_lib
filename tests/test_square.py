import unittest
from square import area, perimeter


class TestSquareFunctions(unittest.TestCase):
    def test_area(self):
        # Arrange
        a = 4
        expected_result = 16

        # Act
        result = area(a)

        # Assert
        self.assertAlmostEqual(result, expected_result)

    def test_perimeter(self):
        # Arrange
        a = 5
        expected_result = 20

        # Act
        result = perimeter(a)

        # Assert
        self.assertAlmostEqual(result, expected_result)

    def test_incorrect_area(self):
        a = -1
        with self.assertRaises(ValueError):
            area(a)

    def test_incorrect_perimeter(self):
        a = -1
        with self.assertRaises(ValueError):
            perimeter(a)


if __name__ == "__main__":
    unittest.main()
