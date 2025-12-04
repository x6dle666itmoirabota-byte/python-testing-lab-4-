import unittest
from geometry import rectangle_area, rectangle_perimeter

class TestRectangleFunctions(unittest.TestCase):

    def test_rectangle_area_positive_numbers(self):
        """Тест для rectangle_area с положительными числами (RT-01)"""
        self.assertEqual(rectangle_area(10, 5), 50)

    def test_rectangle_area_with_zero(self):
        """Тест для rectangle_area с нулевым значением (RT-02)"""
        self.assertIsNone(rectangle_area(0, 5))

    def test_rectangle_area_with_negative(self):
        """Тест для rectangle_area с отрицательным значением (RT-03)"""
        self.assertIsNone(rectangle_area(-10, 5))

    def test_rectangle_area_with_floats(self):
        """Тест для rectangle_area с дробными числами (RT-04)"""
        self.assertAlmostEqual(rectangle_area(2.5, 4), 10.0)

    def test_rectangle_perimeter_positive_numbers(self):
        """Тест для rectangle_perimeter с положительными числами (RT-05)"""
        self.assertEqual(rectangle_perimeter(10, 5), 30)

    def test_rectangle_perimeter_square(self):
        """Тест для rectangle_perimeter для квадрата (RT-06)"""
        self.assertEqual(rectangle_perimeter(7, 7), 28)

    def test_rectangle_perimeter_with_zero(self):
        """Тест для rectangle_perimeter с нулевым значением (RT-07)"""
        self.assertIsNone(rectangle_perimeter(10, 0))

    def test_rectangle_perimeter_with_string(self):
        """Тест для rectangle_perimeter с некорректным типом данных (RT-08)"""
        self.assertIsNone(rectangle_perimeter('a', 5))

if __name__ == '__main__':
    unittest.main()