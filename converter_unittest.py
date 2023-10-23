import unittest
from converter import fahrenheit


class TestCelsius(unittest.TestCase):
    def test_conversion(self):
        self.assertEqual(fahrenheit(27), 27*(9/5)+32)
        self.assertEqual(fahrenheit(0), 32)
        self.assertEqual(fahrenheit(-4), (-4)*(9/5)+32)

    def test_exception(self):
        self.assertRaises(TypeError, fahrenheit, True)
        self.assertRaises(TypeError, fahrenheit, "34")


unittest.main()
