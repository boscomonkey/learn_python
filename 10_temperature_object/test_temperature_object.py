#!/usr/bin/env python

# Example rerun command:
#	rerun -p '*.py' -cx -- python test_temperature_object.py -v


from temperature import Temperature
import unittest

class TestTemperature(unittest.TestCase):

    def test_010_fahrenheit_at_50_degrees(self):
        t = Temperature(f=50)
        self.assertEqual(t.in_fahrenheit(), 50,
                             'at 50 degrees fahrenheit')

    def test_020_fahrenheit_at_freezing(self):
        t = Temperature(f=32)
        self.assertEqual(t.in_celsius(), 0,
                             '32 degrees fahrenheit at 0 celsius')

    def test_030_fahrenheit_at_boiling(self):
        t = Temperature(f=212)
        self.assertEqual(t.in_celsius(), 100,
                             '212 fahrenheit should equal 100 celsius')

    def test_040_fahrenheit_at_body(self):
        t = Temperature(f=98.6)
        self.assertEqual(t.in_celsius(), 37,
                             '98.6 fahrenheit should equal 37 celsius')

    def test_050_fahrenheit_at_arbitrary(self):
        t = Temperature(f=68)
        self.assertEqual(t.in_celsius(), 20,
                             '68 fahrenheit should equal 20 celsius')

    def test_060_celsius_at_50_degrees(self):
        t = Temperature(c=50)
        self.assertEqual(t.in_celsius(), 50,
                             'should equal 50 degrees celsius')

    def test_070_celsius_at_freezing(self):
        self.assertEqual(Temperature(c=0).in_fahrenheit(), 32,
                             '0 c should equal 32 f')

    def test_080_celsius_at_boiling(self):
        self.assertEqual(Temperature(c=100).in_fahrenheit(), 212,
                             '100 c should equal 212 f')

    def test_090_celsius_at_body_temperature(self):
        self.assertEqual(Temperature(c=37).in_fahrenheit(), 98.6,
                             '37 c should equal 98.6 f')

    def test_100_factory_in_degrees_celsius(self):
        self.assertEqual(Temperature.from_celsius(50).in_celsius(), 50,
                             '50 c should equal 50 c')
        self.assertEqual(Temperature.from_celsius(50).in_fahrenheit(), 122,
                             '50 c should equal 122 f')

    def test_110_factory_in_degrees_fahrenheit(self):
        self.assertEqual(Temperature.from_fahrenheit(50).in_fahrenheit(), 50,
                             '50 f should equal 50 f')
        self.assertEqual(Temperature.from_fahrenheit(50).in_celsius(), 10,
                             '50 f should equal 10 c')


if __name__ == '__main__':
    unittest.main()
