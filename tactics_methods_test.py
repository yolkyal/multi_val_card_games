import unittest
from cards import Card
from card_game import MultiValCardGame, Player, Action
from tactics_methods import tactic_play_highest_card, tactic_play_lowest_card, tactic_play_random_card, tactic_play_lowest_winning_card


class TestTacticsMethods(unittest.TestCase):

	def setUp(self):
		self.player1 = Player('Player 1', [Card(4, 1), Card(2, 1)])
		self.player2 = Player('Player 2', [Card(1, 1), Card(3, 1)])
		self.players = [self.player1, self.player2]
		self.game = MultiValCardGame(self.players)

	def test_highest_card(self):
		self.assertEqual(tactic_play_highest_card(self.game, self.player1), Action(self.player1, Card(4, 1)))
		self.assertEqual(tactic_play_highest_card(self.game, self.player2), Action(self.player2, Card(3, 1)))

	def test_lowest_card(self):
		self.assertEqual(tactic_play_lowest_card(self.game, self.player1), Action(self.player1, Card(2, 1)))
		self.assertEqual(tactic_play_lowest_card(self.game, self.player2), Action(self.player2, Card(1, 1)))

	def test_random_card_single(self):
		self.player1.cards = [Card(1, 1)]
		self.assertEqual(tactic_play_random_card(self.game, self.player1), Action(self.player1, Card(1, 1)))

	def test_play_lowest_winning_card(self):
		self.game.round_start()
		self.game.apply_action(Action(self.player1, Card(4, 1)))
		self.assertEqual(tactic_play_lowest_winning_card(self.game, self.player2), Action(self.player2, Card(1, 1)))
		self.game.round_end()

		self.game.round_start()
		self.game.apply_action(Action(self.player1, Card(2, 1)))
		self.assertEqual(tactic_play_lowest_winning_card(self.game, self.player2), Action(self.player2, Card(3, 1)))

if __name__ == '__main__':
	unittest.main()