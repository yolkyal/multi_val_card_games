import unittest
from cards import Card, CardGenerator


class TestCards(unittest.TestCase):

	def test_card_generator(self):
		cards = CardGenerator.generate([1, 2], [3, 4])
		self.assertEqual(cards, [Card(1, 3), Card(1, 4), Card(2, 3), Card(2, 4)])

	def test_get_highest(self):
		pass

	def test_get_lowest(self):
		pass

	def test_get_random_single(self):
		pass


if __name__ == '__main__':
	unittest.main()