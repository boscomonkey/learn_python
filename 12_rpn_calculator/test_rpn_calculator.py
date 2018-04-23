#!/usr/bin/env python

# This driver is executable from the command line.  Use the Python
# "rerun" package to re-run the driver whenever files in this
# directory (and its recursive children) are changed or added.
#
#   rerun -v ./test_rpn_calculator.py


from rpn_calculator import RpnCalculator, CalculatorIsEmpty
import unittest


class TestRpnCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = RpnCalculator()

    def test_010_adds_two_numbers(self):
        self.calc.push(2)
        self.calc.push(3)
        self.calc.plus()
        self.assertEqual(self.calc.value(), 5)

    def test_020_adds_three_numbers(self):
        self.calc.push(2)
        self.calc.push(3)
        self.calc.push(4)
        self.calc.plus()
        self.assertEqual(self.calc.value(), 7)
        self.calc.plus()
        self.assertEqual(self.calc.value(), 9)

    def test_030_subtracts_second_number_from_first_number(self):
        self.calc.push(2)
        self.calc.push(3)
        self.calc.minus()
        self.assertEqual(self.calc.value(), -1)

    def test_040_adds_and_subtracts(self):
        self.calc.push(2)
        self.calc.push(3)
        self.calc.push(4)
        self.calc.minus()
        self.assertEqual(self.calc.value(), -1)
        self.calc.plus()
        self.assertEqual(self.calc.value(), 1)

    def test_050_multiplies_and_divides(self):
        self.calc.push(2)
        self.calc.push(3)
        self.calc.push(4)
        self.calc.divide()
        self.assertEqual(self.calc.value(), 3.0/4.0)
        self.calc.times()
        self.assertEqual(self.calc.value(), 2.0 * (3.0/4.0))

    def test_060_resolves_operator_precedence_unambiguously(self):
        """
        1 2 + 3 * => (1 + 2) * 3
        """
        self.calc.push(1)
        self.calc.push(2)
        self.calc.plus()
        self.calc.push(3)
        self.calc.times()
        self.assertEqual(self.calc.value(), 9)

        # 1 2 3 * + => 1 + (2 * 3)
        self.calc.push(1)
        self.calc.push(2)
        self.calc.push(3)
        self.calc.times()
        self.calc.plus()
        self.assertEqual(self.calc.value(), 7)

    def test_070_fails_informatively_when_theres_not_enough_values(self):
        self.assertRaises(CalculatorIsEmpty, self.calc.plus)
        self.assertRaises(CalculatorIsEmpty, self.calc.minus)
        self.assertRaises(CalculatorIsEmpty, self.calc.times)
        self.assertRaises(CalculatorIsEmpty, self.calc.divide)


if __name__ == '__main__':
    unittest.main()
