#!/usr/bin/env python

# This driver is executable from the command line.  Use the Python
# "rerun" package to re-run the driver whenever files in this
# directory (and its recursive children) are changed or added.
#
#   rerun -v ./test_hello.py

import unittest
from hello import greet, hello

class TestHello(unittest.TestCase):

    def test_010_hello(self):
        self.assertEqual(hello(), 'Hello', 'says hello')

    def test_020_greet(self):
        self.assertEqual(greet('Alice'), 'Hello, Alice!', 'greet someone')
        
    def test_030_greet_another(self):
        self.assertEqual(greet('Bob'), 'Hello, Bob!', 'greet someone else')

if __name__ == '__main__':
    unittest.main()
