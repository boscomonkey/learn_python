#!/usr/bin/env python

# This driver is executable from the command line.  Use the Python
# "rerun" package to re-run the driver whenever files in this
# directory (and its recursive children) are changed or added.
#
#   rerun -v ./test_hello_friend.py


from friend import Friend
import unittest

class TestFriend(unittest.TestCase):

    def test_010_says_hello(self):
        msg = Friend().greeting()
        self.assertEqual(msg, 'Hello!', 'says hello')

    def test_020_says_hello_to_someone(self):
        msg = Friend().greeting('Bob')
        self.assertEqual(msg, 'Hello, Bob!', 'says hello to someone')


if __name__ == '__main__':
    unittest.main()
