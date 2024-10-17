import unittest

from src.calculator import add, subtract, product, divide


class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)


    def test_add_negative(self):
        self.assertEqual(add(-1, -1), -2)


    def test_add_float(self):
        self.assertAlmostEqual(add(1.1, 2.2), 3.3, places=7)


    def test_subtract(self):
        self.assertEqual(subtract(5, 2), 3)


    def test_subtract_negative(self):
        self.assertEqual(subtract(-1, -1), 0)


    def test_subtract_float(self):
        self.assertEqual(subtract(5.5, 2.2), 3.3)


    def test_product(self):
        self.assertEqual(product(5, 2), 10)


    def test_product_negative(self):
        self.assertEqual(product(-1, -1), 1)


    def test_product_float(self):
        self.assertEqual(product(5.5, 2), 11)


    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)


    def test_divide_negative(self):
        self.assertEqual(divide(-10, -2), 5)


    def test_divide_float(self):
        self.assertEqual(divide(10, 3), 3.3333333333333335)


    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)


if __name__ == '__main__':
    unittest.main()
