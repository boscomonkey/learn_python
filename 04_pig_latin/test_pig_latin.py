#!/usr/bin/env python

# Example rerun command:
#	rerun -p '*.py' -cx -- ./test_pig_latin.py -v

import unittest
from pig_latin import translate

# # Topics
#
# * modules
# * strings
#
# # Pig Latin
#
# Pig Latin is a made-up children's language that's intended to be confusing. It obeys a few simple rules (below) but when it's spoken quickly it's really difficult for non-children (and non-native speakers) to understand.
#
# Rule 1: If a word begins with a vowel sound, add an "ay" sound to the end of the word.
#
# Rule 2: If a word begins with a consonant sound, move it to the end of the word, and then add an "ay" sound to the end of the word.
#
# (There are a few more rules for edge cases, and there are regional variants too, but that should be enough to understand the tests.)
#
# See <http://en.wikipedia.org/wiki/Pig_latin> for more details.
#
#

class TestPigLatin(unittest.TestCase):

    def test_translates_a_word_beginning_with_a_vowel(self):
        self.assertEqual(translate('apple'), 'appleay')

    def test_translates_a_word_beginning_with_a_consonant(self):
        self.assertEqual(translate('banana'), 'ananabay')

    def test_translates_a_word_beginning_with_two_consonants(self):
        self.assertEqual(translate('cherry'), 'errychay')

    def test_translates_two_words(self):
        self.assertEqual(translate('eat pie'), 'eatay iepay')

    def test_translates_a_word_beginning_with_three_consonants(self):
        self.assertEqual(translate('three'), 'eethray')

    def test_counts_sch_as_single_phoneme(self):
        self.assertEqual(translate('school'), 'oolschay')

    def test_counts_qu_as_single_phoneme(self):
        self.assertEqual(translate('quiet'), 'ietquay')

    def test_counts_qu_as_single_phoneme_even_when_preceded_by_consonant(self):
        self.assertEqual(translate('square'), 'aresquay')

    def test_translates_many_words(self):
        self.assertEqual(translate('the quick brown fox'), 'ethay ickquay ownbray oxfay')

    # Test-driving bonus:
    # * write a test asserting that capitalized words are still capitalized (but with a different initial capital letter, of course)
    # * retain the punctuation from the original phrase

    def test_translates_capitalized_words(self):
        self.assertEqual(translate('Apple'), 'Appleay')
        self.assertEqual(translate('Banana'), 'Ananabay')
        self.assertEqual(translate('Cherry'), 'Errychay')
        self.assertEqual(translate('Eat Pie'), 'Eatay Iepay')
        self.assertEqual(translate('Three'), 'Eethray')
        self.assertEqual(translate('School'), 'Oolschay')
        self.assertEqual(translate('Quiet'), 'Ietquay')
        self.assertEqual(translate('Square'), 'Aresquay')
        self.assertEqual(translate('The Quick Brown Fox'), 'Ethay Ickquay Ownbray Oxfay')

    def test_retains_punctuation_from_original_phrase(self):
        self.assertEqual(translate('Apple!'), 'Appleay!')
        self.assertEqual(translate('Banana!!'), 'Ananabay!!')
        self.assertEqual(translate('Cherry!!!'), 'Errychay!!!')
        self.assertEqual(translate('Eat Pie!!!!'), 'Eatay Iepay!!!!')
        self.assertEqual(translate('Three.'), 'Eethray.')
        self.assertEqual(translate('School?'), 'Oolschay?')
        self.assertEqual(translate('Quiet...'), 'Ietquay...')
        self.assertEqual(translate('Square???'), 'Aresquay???')
        self.assertEqual(translate('The Quick Brown Fox!'), 'Ethay Ickquay Ownbray Oxfay!')


if __name__ == '__main__':
    unittest.main()
