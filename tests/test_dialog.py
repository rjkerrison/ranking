from unittest.mock import patch
from unittest import TestCase

from classes.ranking import Ranking

class Test(TestCase):
  def setUp(self):
    self.ranking = Ranking(
      "pasta",
      {
        "name": "The name of the pasta",
        "shape": "A description of the shape",
        "price": "The price of the pasta per kilogram"
      },
      [
        {
          "name": "spaghetti",
          "shape": "long cylindrical strands",
          "price": "1.40",
          "_id": "9ffec3ab13c2ae87118341f6a6adc7dc8459784bb0068c30a361249ba23c3cce"
        },
        {
          "name": "penne",
          "shape": "hollow cylinders with grooves on the outside and sloped ends",
          "price": "1.60",
          "_id": "0cefddfc01cb1aff08c864c2bc1b256eb4cde17a6a8e6c5587312caf3bb97773"
        },
        {
          "name": "conchiglie",
          "shape": "shells with grooves on the outside",
          "price": "3.40",
          "_id": "6ea18ff6a4a435c64e7f7ea28f826d33f912202f20f0f6a4a01746dcabf9e0f6"
        }
      ],
      [
        "9ff>6ea"
      ]
    )

  def test_loaded_rank_data(self):
    self.assertEqual(len(self.ranking.rank_data), 1)
    self.assertEqual(self.ranking.rank_data[0], "9ff>6ea")

  def test_loaded_entries(self):
    self.assertEqual(len(self.ranking.entries), 3)
    self.assertEqual(self.ranking.entries[0]['name'], "spaghetti")
    self.assertEqual(self.ranking.entries[1]['name'], "penne")
    self.assertEqual(self.ranking.entries[2]['name'], "conchiglie")

  @patch('classes.ranking.get_input', return_value='9ff<0ce')
  def test_add_comparison(self, get_input):
    self.ranking.add_comparison()

    self.assertEqual(len(self.ranking.rank_data), 2)
    self.assertEqual(self.ranking.rank_data[0], "9ff>6ea")
    self.assertEqual(self.ranking.rank_data[1], "9ff<0ce")

  @patch('classes.ranking.get_input', return_value='fusilli')
  def test_add_entry(self, get_input):
    self.ranking.add_entry()

    self.assertEqual(len(self.ranking.entries), 4)
