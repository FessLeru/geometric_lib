import unittest
from square import area, perimeter


class SquareTestCase(unittest.TestCase):
    """Тесты для модуля square.py"""

    def test_area_zero(self):
        """Тест площади квадрата с нулевой стороной"""
        res = area(0)
        self.assertEqual(res, 0)

    def test_area_standard(self):
        """Тест площади квадрата со стандартным значением"""
        res = area(10)
        self.assertEqual(res, 100)

    def test_perimeter_zero(self):
        """Тест периметра квадрата с нулевой стороной"""
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter_standard(self):
        """Тест периметра квадрата со стандартным значением"""
        res = perimeter(10)
        self.assertEqual(res, 40)


if __name__ == '__main__':
    unittest.main()

