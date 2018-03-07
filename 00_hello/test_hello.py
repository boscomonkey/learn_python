#!/usr/bin/env python

import unittest
from hello import greet, hello

class TestHello(unittest.TestCase):

    def test_hello(self):
        self.assertEqual(hello(), 'Hello', 'says hello')

    def test_greet(self):
        self.assertEqual(greet('Alice'), 'Hello, Alice!', 'greet someone')
        
    def test_greet_another(self):
        self.assertEqual(greet('Bob'), 'Hello, Bob!', 'greet someone else')

if __name__ == '__main__':
    unittest.main()
