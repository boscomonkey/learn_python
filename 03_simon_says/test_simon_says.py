#!/usr/bin/env python

# This driver is executable from the command line.  Use the Python
# "rerun" package to re-run the driver whenever files in this
# directory (and its recursive children) are changed or added.
#
#   rerun -v ./test_simon_says.py

import unittest
from simon_says import echo, shout, repeat, start_of_word, first_word, titleize

class TestSimonSays(unittest.TestCase):

    def test_010_echo(self):
        self.assertEqual(echo('hello'), 'hello')

    def test_020_echo_bye(self):
        self.assertEqual(echo('bye'), 'bye')

    def test_030_shout_hello(self):
        self.assertEqual(shout('hello'), 'HELLO')

    def test_040_shout_hello_world(self):
        self.assertEqual(shout('hello world'), 'HELLO WORLD')

    def test_050_repeat(self):
        self.assertEqual(repeat('hello'), 'hello hello')

    def test_060_repeat_a_number_of_times(self):
        """
        Wait a second! How can you make the "repeat" method
        take one *or* two arguments?

        Hint: *default values*
        """
        self.assertEqual(repeat('hello', 3), 'hello hello hello')

    def test_070_repeat_zero_times(self):
        self.assertEqual(repeat('hello', 0), '')

    def test_080_first_letter(self):
        self.assertEqual(start_of_word('hello', 1), 'h')

    def test_090_first_two_letters(self):
        self.assertEqual(start_of_word('Bob', 2), 'Bo')

    def test_100_first_several_letters(self):
        str = 'abcdefg'
        self.assertEqual(start_of_word(str, 1), 'a')
        self.assertEqual(start_of_word(str, 2), 'ab')
        self.assertEqual(start_of_word(str, 3), 'abc')

    def test_110_hello_world(self):
        self.assertEqual(first_word('Hello World'), 'Hello')

    def test_120_oh_dear(self):
        self.assertEqual(first_word('oh dear'), 'oh')

    def test_130_capitalizes_a_word(self):
        self.assertEqual(titleize('jaws'), 'Jaws')

    def test_140_capitalizes_every_word(self):
        self.assertEqual(titleize('david copperfield'), 'David Copperfield')

    def test_150_doesnt_capitalizes_little_words(self):
        self.assertEqual(titleize('war and peace'), 'War and Peace')

    def test_160_does_capitalizes_little_words_at_start_of_title(self):
        self.assertEqual(titleize('the bridge over the river kwai'), 'The Bridge over the River Kwai')


if __name__ == '__main__':
    unittest.main()
