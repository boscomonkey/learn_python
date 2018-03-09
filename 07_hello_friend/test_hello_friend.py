#!/usr/bin/env python

# Example rerun command:
#	rerun -p '*.py' -cx -- python test_hello_friend.py -v


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
