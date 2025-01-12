import unittest
from unittest import TestCase
from basic_calculator import BasicCalculator

class TestBasicCalculator(TestCase):
    def test_add(self):
        calculator = BasicCalculator((1, 2, 3))
        self.assertEqual(calculator.add(), 6)
        
    def test_subtract(self):
        calculator = BasicCalculator((10, 2, 3))
        self.assertEqual(calculator.subtract(), 5)
        
    def test_multiply(self):
        calculator = BasicCalculator((2, 3, 4))
        self.assertEqual(calculator.multiply(), 24)
    
    def test_zero_multiply(self):
        calculator = BasicCalculator((2, 3, 4, 0))
        self.assertEqual(calculator.multiply(), 0)
        
    def test_divide(self):
        calculator = BasicCalculator((100, 2, 5))
        self.assertEqual(calculator.divide(), 10)
    
    def test_divide_by_zero(self):
        calculator = BasicCalculator((100, 2, 5, 0))
        self.assertEqual(calculator.divide(), 'Cannot divide by zero' )
    
    def test_zero_divide(self):
        calculator = BasicCalculator((0, 100, 2, 5))
        self.assertEqual(calculator.divide(), 0)

if __name__ == "__main__":
    unittest.main()