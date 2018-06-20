#!/usr/bin/env python

# This driver is executable from the command line.  Use the Python
# "rerun" package to re-run the driver whenever files in this
# directory (and its recursive children) are changed or added.
#
#   rerun -v ./test_dictionary.py


from dictionary import Dictionary
import unittest


class TestDictionary(unittest.TestCase):

    def setUp(self):
        self.d = Dictionary()

    def test_010_is_empty_when_created(self):
        self.assertEqual(self.d.entries(), {})

    def test_020_can_add_whole_entries_with_keyword_and_definition(self):
        self.d.add('fish', 'aquatic animal')
        self.assertEqual(self.d.entries(), {'fish': 'aquatic animal'})
        self.assertEqual(self.d.keywords(), ['fish'])

    def test_030_add_keywords_without_definition(self):
        self.d.add('fish')
        self.assertEqual(self.d.entries(), {'fish': None})
        self.assertEqual(self.d.keywords(), ['fish'])

    def test_040_can_check_whether_a_given_keyword_exists(self):
        self.assertFalse(self.d.includes('fish'))

    def test_050_doesnt_cheat_when_checking_whether_keyword_exists(self):
        self.assertFalse(self.d.includes('fish'))
        self.d.add('fish')
        self.assertTrue(self.d.includes('fish'))
        self.assertFalse(self.d.includes('bird'))

    def test_060_doesnt_include_a_prefix_in_and_of_itself(self):
        self.d.add('fish')
        self.assertFalse(self.d.includes('fi'))

    def test_070_doesnt_find_a_word_in_an_empty_dictionary(self):
        self.assertFalse(self.d.includes('fi'))

    def test_080_finds_nothing_if_the_prefix_matches_nothing(self):
        self.d.add('fiend')
        self.d.add('great')
        self.assertEqual(len(self.d.find('nothing')), 0)

    def test_090_finds_an_entry(self):
        self.d.add('fish', 'aquatic animal')
        self.assertEqual(self.d.find('fish'), {'fish': 'aquatic animal'})

    def test_100_finds_multiple_matches_from_a_prefix_and_returns_the_entire_entry(self):
        self.d.add('fish', 'aquatic animal')
        self.d.add('fiend', 'wicked person')
        self.d.add('great', 'remarkable')
        self.assertEqual(self.d.find('fi'),
                         {
                             'fish': 'aquatic animal',
                             'fiend': 'wicked person'
                         })

    def test_110_lists_keywords_alphabetically(self):
        self.d.add('zebra', 'African land animal with stripes')
        self.d.add('fish', 'aquatic animal')
        self.d.add('apple', 'fruit')
        self.assertEqual(self.d.keywords(),
                         ['apple', 'fish', 'zebra'])

    def test_120_can_produce_printable_output(self):
        self.d.add('zebra', 'African land animal with stripes')
        self.d.add('fish', 'aquatic animal')
        self.d.add('apple', 'fruit')
        should_str = """[apple] \"fruit\"
[fish] \"aquatic animal\"
[zebra] \"African land animal with stripes\""""
        self.assertEqual(self.d.printable(), should_str)


if __name__ == '__main__':
    unittest.main()
