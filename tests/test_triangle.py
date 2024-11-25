import unittest
from triangle import area, perimeter


class TestTriangleFunctions(unittest.TestCase):
    def test_area(self):
        # Arrange
        a, h = 5, 10
        expected_result = 25

        # Act
        result = area(a, h)

        # Assert
        self.assertEqual(result, expected_result)

    def test_perimeter(self):
        # Arrange
        a, b, c = 3, 4, 5
        expected_result = 12

        # Act
        result = perimeter(a, b, c)

        # Assert
        self.assertEqual(result, expected_result)

    def test_incorrect_area(self):
        a, h = -1, 0
        with self.assertRaises(ValueError):
            area(a, h)

    def test_incorrect_perimeter(self):
        a, b, c = -1, 0, 1
        with self.assertRaises(ValueError):
            perimeter(a, b, c)


if __name__ == "__main__":
    unittest.main()
