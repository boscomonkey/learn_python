#!/usr/bin/env python

# Example rerun command:
#	rerun -p '*.py' -cx -- python test_timer.py -v


from timer import Timer
import unittest

class TestTimer(unittest.TestCase):

    def setUp(self):
        self.timer = Timer()

    def test_010_initializes_to_0_seconds(self):
        self.assertEqual(self.timer.seconds, 0,
                             'should initialize to 0 seconds')

    def test_020_time_string_displays_0_seconds(self):
        self.assertEqual(self.timer.time_string(), '00:00:00',
                             'should display 0 seconds as 00:00:00')

    def test_030_time_string_displays_12_seconds(self):
        self.timer.seconds = 12
        self.assertEqual(self.timer.time_string(), '00:00:12',
                             'should display 12 seconds as 00:00:12')

    def test_040_time_string_displays_66_seconds(self):
        self.timer.seconds = 66
        self.assertEqual(self.timer.time_string(), '00:01:06',
                             'should display 66 seconds as 00:01:06')

    def test_050_time_string_displays_4000_seconds(self):
        self.timer.seconds = 4000
        self.assertEqual(self.timer.time_string(), '01:06:40',
                             'should display 4000 seconds as 01:06:40')


if __name__ == '__main__':
    unittest.main()
