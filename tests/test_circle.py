import unittest
from circle import area, perimeter

class TestSquareFunctions(unittest.TestCase):
    def test_area(self):
        # Arrange
        r = 3
        expected_result = math.pi * r * r

        # Act
        result = area(r)

        # Assert
        self.assertAlmostEqual(result, expected_result)

    def test_perimeter(self):
        # Arrange
        r = 3
        expected_result = 2 * math.pi * r

        # Act
        result = perimeter(r)

        # Assert
        self.assertAlmostEqual(result, expected_result)

if __name__ == "__main__":
    unittest.main()