import unittest
import json
from classes.contest import Contest

class TestContest(unittest.TestCase):
    def test_both_constructors_are_equal(self):
        a = Contest(1, 4, '>')
        b = Contest(None, None, '>', contestors = (4, 1))

        self.assertEqual(a, b)

    def test_from_json(self):
        j = json.loads(r'{"contestors": [1,4], "outcome": ">"}')
        a = Contest(**j)

        self.assertEqual(frozenset({1,4}), a.contestors)
        self.assertEqual('>', a.outcome)

    def test_as_json(self):
        a = Contest(1, 4, '>')
        j = json.loads(a.as_json())

        self.assertEqual([1,4], j['contestors'])
        self.assertEqual('>', j['outcome'])

if __name__ == '__main__':
    unittest.main()
