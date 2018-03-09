#!/usr/bin/env python

# Example rerun command:
#	rerun -p '*.py' -cx -- python test_book_titles.py -v


from book import Book
import unittest

class TestTitle(unittest.TestCase):

    def setUp(self):
        self.book = Book()

    def test_010_capitalize_first_letter(self):
        self.book.title = 'inferno'
        self.assertEqual(self.book.title, 'Inferno',
                             'should capitalize the first letter')

    def test_020_capitalize_every_word(self):
        self.book.title = 'stuart little'
        self.assertEqual(self.book.title, 'Stuart Little',
                             'should capitalize every word')


class TestTitleCapitalizationExcept(unittest.TestCase):

    def setUp(self):
        self.book = Book()

    def test_010_articles_the(self):
        self.book.title = 'alexander the great'
        self.assertEqual(self.book.title, 'Alexander the Great',
                             'should capitalize every word except... the')

    def test_020_articles_a(self):
        self.book.title = 'to kill a mockingbird'
        self.assertEqual(self.book.title, 'To Kill a Mockingbird',
                             'should capitalize every word except... a')

    def test_030_articles_an(self):
        self.book.title = 'to eat an apple a day'
        self.assertEqual(self.book.title, 'To Eat an Apple a Day',
                             'should capitalize every word except... an')

    def test_040_conjunctions(self):
        self.book.title = 'war and peace'
        self.assertEqual(self.book.title, 'War and Peace',
                             'should capitalize every word except... conjunctions')

    def test_050_prepositions(self):
        self.book.title = 'love in the time of cholera'
        self.assertEqual(self.book.title, 'Love in the Time of Cholera',
                             'should capitalize every word except... prepositions')


class TestTitleCapitalizationNoExceptions(unittest.TestCase):

    def setUp(self):
        self.book = Book()

    def test_010_pronoun_i(self):
        self.book.title = 'what i wish i knew when i was 20'
        self.assertEqual(self.book.title, 'What I Wish I Knew When I Was 20',
                             'should always capitalize... I')

    def test_020_the_first_word(self):
        self.book.title = 'the man in the iron mask'
        self.assertEqual(self.book.title, 'The Man in the Iron Mask',
                             'should always capitalize... the first word')

if __name__ == '__main__':
    unittest.main()
