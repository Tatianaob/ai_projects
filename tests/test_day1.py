# test for calculator

# import unittest
# import day1

# class TestCalculatorFunactions(unittest.TestCase):

#     def test_add(self):
#         self.assertEqual(day1.add(2, 3), 5)
#         self.assertEqual(day1.add(4, 8), 12)
#         self.assertEqual(day1.add(-1, 1), 0)

#     def test_substract(self):
#         self.assertEqual(day1.substract(10, 3), 7)
#         self.assertEqual(day1.substract(-1,-1), 0)

#     def test_multiple(self):
#         self.assertEqual(day1.multiply(3, 4), 12)
#         self.assertEqual(day1.multiply(-1, 5), -5)
    
#     def test_divide(self):
#         self.assertEqual(day1.divide(10,2), 5)
#         self.assertEqual(day1.divide(5, 0), "Error! Division by zero not allowed")

# if __name__ == "__main__":
#     unittest.main()



#pytest:
import pytest
import src.day1 as day1

def test_add():
    assert day1.add(2, 3) == 5
    assert day1.add(50, 45) == 95

def test_substract():
    assert day1.substract(90, 1) == 89
    assert day1.substract(6, 3) == 3

def test_multiply():
    assert day1.multiply(4, 5) == 20
    assert day1.multiply(5, 0) == 0

def test_divide():
    assert day1.divide(10, 2) == 5
    assert day1.divide(5, 0) == "Error! Division by zero not allowed"