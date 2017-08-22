import unittest
from classes.comparison import *

class TestStringMethods(unittest.TestCase):
    def __init__(self, param):
        self.comparison_builder = ComparisonBuilder()
        super().__init__(param)

    def test_pair_arguments(self):
        comparison_list = self.comparison_builder.build_comparison(['a','b'], Ordering.OneBeatsTwo)
        comparison_tuple = self.comparison_builder.build_comparison(('a','b'), Ordering.OneBeatsTwo)
        comparison_generator = self.comparison_builder.build_comparison((a for a in ['a','b']), Ordering.OneBeatsTwo)

        self.assertEqual(comparison_list, comparison_tuple)
        self.assertEqual(comparison_list, comparison_generator)

    def test_choice_argument(self):
        comparison_ordering = self.comparison_builder.build_comparison(['a','b'], Ordering.OneBeatsTwo)
        comparison_int = self.comparison_builder.build_comparison(['a','b'], -1)

        self.assertEqual(comparison_ordering, comparison_int)

    def test_split(self):
        with self.assertRaises(Exception):
            self.comparison_builder.build_comparison(['a','b','c'], Ordering.OnAPar)

if __name__ == '__main__':
    unittest.main()
