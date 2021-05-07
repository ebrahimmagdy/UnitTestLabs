import unittest
import calculator

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculator.add(3, 4), 7)


    def test_substract(self):
        self.assertEqual(calculator.substract(10, 3), 7)

    def test_multibly(self):
        self.assertEqual(calculator.multibly(10, 7), 70)

    def test_divide(self):
        self.assertEqual(calculator.divide(10, 5), 2)

    def test_divide_over_zero(self):
        self.assertRaises(ValueError, calculator.divide, 1, 0)

if __name__ == '__main__':
    unittest.main()