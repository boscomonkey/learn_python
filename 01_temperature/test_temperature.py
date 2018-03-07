#!/usr/bin/env python

# Example rerun command:
#	rerun -p '*.py' -cx -- ./test_temperature.py -v

import unittest
from temperature import ftoc, ctof

class TestFahrenheitToCentigrade(unittest.TestCase):

    def test_freezing_temperature(self):
        self.assertEqual(ftoc(32), 0)

    def test_boiling_temperature(self):
        self.assertEqual(ftoc(212), 100)

    def test_body_temperature(self):
        self.assertEqual(ftoc(98.6), 37)

    def test_arbitrary_temperature(self):
        self.assertEqual(ftoc(68), 20)

class TestCentigradeToFahrenheit(unittest.TestCase):

    def test_freezing_temperature(self):
        self.assertEqual(ctof(0), 32)

    def test_boiling_temperature(self):
        self.assertEqual(ctof(100), 212)

    def test_arbitrary_temperature(self):
        self.assertEqual(ctof(20), 68)

    def test_body_temperature(self):
        self.assertEqual(ctof(37), 98.6)

if __name__ == '__main__':
    unittest.main()
