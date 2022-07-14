import unittest
from month import Word
from functions import retrieve_random_month


class MonthsProgramTest(unittest.TestCase):

    def setUp(self):
        self.new_word = Word()
        self.list_12_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    # checking weather random range in 12
    def test_retrieved_number(self):
        number = retrieve_random_month()
        self.assertIn(number, self.list_12_numbers)
