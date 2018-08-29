import unittest
from classes.comparison import ComparisonBuilder, Ordering

class TestStringMethods(unittest.TestCase):
    def setUp(self):
        self.comparison_builder = ComparisonBuilder()

    def test_list_and_tuple_generate_same_pair(self):
        comparison_list = self.comparison_builder.build_comparison(
            ['a', 'b'],
            Ordering.OneBeatsTwo)

        comparison_tuple = self.comparison_builder.build_comparison(
            ('a', 'b'),
            Ordering.OneBeatsTwo)

        self.assertEqual(comparison_list.pair, comparison_tuple.pair)

    def test_list_and_generator_generate_same_pair(self):
        comparison_list = self.comparison_builder.build_comparison(
            ['a', 'b'],
            Ordering.OneBeatsTwo)

        comparison_generator = self.comparison_builder.build_comparison(
            (a for a in ['a', 'b']),
            Ordering.OneBeatsTwo)

        self.assertEqual(comparison_list.pair, comparison_generator.pair)

    def test_choice_same_when_int_or_ordering_given(self):
        comparison_ordering = self.comparison_builder.build_comparison(
            ['a', 'b'],
            Ordering.OneBeatsTwo)

        comparison_int = self.comparison_builder.build_comparison(
            ['a', 'b'],
            -1)

        self.assertEqual(comparison_ordering.pair, comparison_int.pair)
        self.assertEqual(comparison_ordering.choice, comparison_int.choice)

    def test_pair_same_when_int_or_ordering_given(self):
        comparison_ordering = self.comparison_builder.build_comparison(
            ['a', 'b'],
            Ordering.OneBeatsTwo)

        comparison_int = self.comparison_builder.build_comparison(
            ['a', 'b'],
            -1)

        self.assertEqual(comparison_ordering.pair, comparison_int.pair)

    def test_too_many_arguments_raises_exception(self):
        with self.assertRaises(Exception):
            self.comparison_builder.build_comparison(
                ['a', 'b', 'c'],
                Ordering.OnAPar)

if __name__ == '__main__':
    unittest.main()
