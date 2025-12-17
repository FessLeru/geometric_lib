import unittest
from triangle import area, perimeter

class TriangleTestCase(unittest.TestCase):
    """Тесты для модуля triangle.py"""
    def test_area_zero(self):
        """Тест площади треугольника с нулевыми сторонами"""
        res = area(0, 0, 0)
        self.assertEqual(res, 0)

    def test_area_standard(self):
        """Тест площади треугольника со стандартными значениями"""
        res = area(3, 4, 5)
        self.assertEqual(res, 6)

    def test_perimeter_zero(self):
        """Тест периметра треугольника с нулевыми сторонами"""
        res = perimeter(0, 0, 0)
        self.assertEqual(res, 0)
    
    def test_perimeter_standard(self):
        """Тест периметра треугольника со стандартными значениями"""
        res = perimeter(3, 4, 5)
        self.assertEqual(res, 15)

    def test_perimeter_negative(self):
        """Тест периметра треугольника с отрицательными сторонами"""
        with self.assertRaises(ValueError):
            area(-3, -4, -5)

    def test_perimeter_float(self):
        """Тест периметра треугольника с дробными сторонами"""
        res = perimeter(2.5, 3.5, 4.5)
        self.assertAlmostEqual(res, 10.5, places=6)