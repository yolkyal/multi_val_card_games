import random
import functools


class Card:
	def __init__(self, val1, val2):
		self.val1 = val1
		self.val2 = val2

	def __hash__(self):
		return hash((val1, val2))

	def __eq__(self, other):
		return type(other) == Card and self.val1 == other.val1 and self.val2 == other.val2

	def __gt__(self, other):
		if self.val1 == other.val1:
			return self.val2 > other.val2
		else:
			return self.val1 > other.val1

	def __str__(self):
		return str(self.val1) + '-' + str(self.val2)

	def __repr__(self):
		return self.__str__()


class CardGenerator:
	def generate(ls_val1, ls_val2):
		return [Card(val1, val2) for val1 in ls_val1 for val2 in ls_val2]


def get_highest(cards):
	return functools.reduce(lambda card1, card2 : card1 if card1 > card2 else card2, cards)


def get_lowest(cards):
	return functools.reduce(lambda card1, card2 : card1 if card1 < card2 else card2, cards)


def get_random(cards):
	return cards[random.randint(0, len(cards) - 1)]
