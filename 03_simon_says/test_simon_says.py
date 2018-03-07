#!/usr/bin/env python

# Example rerun command:
#	rerun -p '*.py' -cx -- ./test_simon_says.py -v

import unittest
from simon_says import echo, shout, repeat, start_of_word, first_word, titleize

class TestSimonSays(unittest.TestCase):

    def test_echo(self):
        self.assertEqual(echo('hello'), 'hello')

    def test_echo_bye(self):
        self.assertEqual(echo('bye'), 'bye')

class TestShout(unittest.TestCase):

    def test_shout_hello(self):
        self.assertEqual(shout('hello'), 'HELLO')

    def test_shout_hello_world(self):
        self.assertEqual(shout('hello world'), 'HELLO WORLD')

class TestRepeat(unittest.TestCase):

    def test_repeat(self):
        self.assertEqual(repeat('hello'), 'hello hello')

    def test_repeat_a_number_of_times(self):
        self.assertEqual(repeat('hello', 3), 'hello hello hello')

    def test_repeat_zero_times(self):
        self.assertEqual(repeat('hello', 0), '')

class TestStartOfWord(unittest.TestCase):

    def test_first_letter(self):
        self.assertEqual(start_of_word('hello', 1), 'h')

    def test_first_two_letters(self):
        self.assertEqual(start_of_word('Bob', 2), 'Bo')

    def test_first_several_letters(self):
        str = 'abcdefg'
        self.assertEqual(start_of_word(str, 1), 'a')
        self.assertEqual(start_of_word(str, 2), 'ab')
        self.assertEqual(start_of_word(str, 3), 'abc')

class TestFirstWord(unittest.TestCase):

    def test_hello_world(self):
        self.assertEqual(first_word('Hello World'), 'Hello')

    def test_oh_dear(self):
        self.assertEqual(first_word('oh dear'), 'oh')

class TestTitleize(unittest.TestCase):

    def test_capitalizes_a_word(self):
        self.assertEqual(titleize('jaws'), 'Jaws')

    def test_capitalizes_every_word(self):
        self.assertEqual(titleize('david copperfield'), 'David Copperfield')

    def test_doesnt_capitalizes_little_words(self):
        self.assertEqual(titleize('war and peace'), 'War and Peace')

    def test_does_capitalizes_little_words_at_start_of_title(self):
        self.assertEqual(titleize('the bridge over the river kwai'), 'The Bridge over the River Kwai')


if __name__ == '__main__':
    unittest.main()
