#!/usr/bin/env python

# Example rerun command:
#	rerun -p '*.py' -cx -- ./test_calculator.py -v

import unittest
from calculator import add, subtract, sum, multiply, power, factorial

class TestAdd(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(0,0), 0)

    def test_adds_2_and_2(self):
        self.assertEqual(add(2,2), 4)

    def test_adds_positive_numbers(self):
        self.assertEqual(add(2,6), 8)

class TestSubtract(unittest.TestCase):

    def test_subtracts_numbers(self):
        self.assertEqual(subtract(10,4), 6)

class TestSum(unittest.TestCase):

    def test_sums_empty_array(self):
        self.assertEqual(sum([]), 0)

    def test_sums_array_of_one_number(self):
        self.assertEqual(sum([7]), 7)

    def test_sums_array_of_two_numbers(self):
        self.assertEqual(sum([7,11]), 18)

    def test_sums_array_of_many_numbers(self):
        self.assertEqual(sum([1,3,5,7,9]), 25)

class TestMultiply(unittest.TestCase):

    def test_multiplies_two_numbers(self):
        self.assertEqual(multiply(0, 0), 0)

    def test_multiplies_several_numbers(self):
        self.assertEqual(multiply(2,3,4,5), 120)

class TestPower(unittest.TestCase):

    def test_raises_one_number_to_the_power_of_another_number(self):
        self.assertEqual(power(2,3), 8)

class TestFactorial(unittest.TestCase):

    def test_factorial_of_0(self):
        self.assertEqual(factorial(0), 1)

    def test_factorial_of_1(self):
        self.assertEqual(factorial(1), 1)

    def test_factorial_of_2(self):
        self.assertEqual(factorial(2), 2)

    def test_factorial_of_5(self):
        self.assertEqual(factorial(5), 120)

    def test_factorial_of_10(self):
        self.assertEqual(factorial(10), 3628800)

if __name__ == '__main__':
    unittest.main()
