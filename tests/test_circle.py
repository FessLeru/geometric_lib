import unittest
import math
from circle import area, perimeter


class CircleTestCase(unittest.TestCase):
    """Тесты для модуля circle.py"""

    def test_area_zero(self):
        """Тест площади круга с нулевым радиусом"""
        res = area(0)
        self.assertEqual(res, 0)

    def test_area_standard(self):
        """Тест площади круга со стандартным значением"""
        res = area(3)
        expected = math.pi * 3 * 3
        self.assertAlmostEqual(res, expected, places=5)

    def test_perimeter_zero(self):
        """Тест периметра круга с нулевым радиусом"""
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter_standard(self):
        """Тест периметра круга со стандартным значением"""
        res = perimeter(3)
        expected = 2 * math.pi * 3
        self.assertAlmostEqual(res, expected, places=5)


if __name__ == '__main__':
    unittest.main()

