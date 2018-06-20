#!/usr/bin/env python

# This driver is executable from the command line.  Use the Python
# "rerun" package to re-run the driver whenever files in this
# directory (and its recursive children) are changed or added.
#
#   rerun -v ./test_temperature.py

import unittest
from temperature import ftoc, ctof

class TestTemperature(unittest.TestCase):

    def test_010_ftoc_freezing_temperature(self):
        self.assertEqual(ftoc(32), 0)

    def test_020_ftoc_boiling_temperature(self):
        self.assertEqual(ftoc(212), 100)

    def test_030_ftoc_body_temperature(self):
        self.assertEqual(ftoc(98.6), 37)

    def test_040_ftoc_arbitrary_temperature(self):
        self.assertEqual(ftoc(68), 20)

    def test_050_ctof_freezing_temperature(self):
        self.assertEqual(ctof(0), 32)

    def test_060_ctof_boiling_temperature(self):
        self.assertEqual(ctof(100), 212)

    def test_070_ctof_arbitrary_temperature(self):
        self.assertEqual(ctof(20), 68)

    def test_080_ctof_body_temperature(self):
        self.assertEqual(ctof(37), 98.6)

if __name__ == '__main__':
    unittest.main()
