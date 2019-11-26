import unittest
from cards import Card
from card_game import MultiValCardGame, Dealer, Player, Action
import pdb


class TestCardGame(unittest.TestCase):

	def setUp(self):
		self.player1 = Player('Player 1')
		self.player2 = Player('Player 2')
		self.game = MultiValCardGame([self.player1, self.player2])

	def test_deal_cards(self):
		players = [Player('Player 1', []), Player('Player 2', [])]
		cards = [Card(1, 1), Card(2, 2), Card(3, 3), Card(4, 4)]
		dealer = Dealer(cards)
		dealer.deal_to(players)
		self.assertEqual(players[0].cards, [Card(1, 1), Card(3, 3)])
		self.assertEqual(players[1].cards, [Card(2, 2), Card(4, 4)])

	def test_get_actions(self):
		self.player1.cards = [Card(1, 1), Card(2, 2)]
		actions = self.game.get_actions(self.player1)
		self.assertEqual(len(actions), 2)
		self.assertEqual(actions, [Action(self.player1, Card(1, 1)), Action(self.player1, Card(2, 2))])

	def test_round_start(self):
		self.game.round_start()
		self.assertTrue(self.game.active_round != None)

	def test_apply_action_with_same_types(self):
		self.player1 = Player('Player 1', [Card(1, 1), Card(1, 3)])
		self.player2 = Player('Player 2', [Card(1, 2), Card(1, 4)])

		self.game.round_start()
		self.game.apply_action(Action(self.player1, Card(1, 1)))
		self.game.apply_action(Action(self.player2, Card(1, 4)))
		self.game.round_end()

		completed_round = self.game.completed_rounds[0]
		self.assertEqual(completed_round.winning_action, Action(self.player2, Card(1, 4)))

		self.game.round_start()
		self.game.apply_action(Action(self.player1, Card(1, 3)))
		self.game.apply_action(Action(self.player2, Card(1, 2)))
		self.game.round_end()

		completed_round = self.game.completed_rounds[1]
		self.assertEqual(completed_round.winning_action, Action(self.player1, Card(1, 3)))

		self.assertEqual(self.player1.cards, [])
		self.assertEqual(self.player2.cards, [])

	def test_apply_action_with_different_types(self):
		self.player1 = Player('Player 1', [Card(2, 1), Card(1, 3)])
		self.player2 = Player('Player 2', [Card(2, 2), Card(1, 4)])

		self.game.round_start()
		self.game.apply_action(Action(self.player1, Card(2, 1)))
		self.game.apply_action(Action(self.player2, Card(1, 4)))
		self.game.round_end()

		completed_round = self.game.completed_rounds[0]
		self.assertEqual(completed_round.winning_action, Action(self.player1, Card(2, 1)))

		self.game.round_start()
		self.game.apply_action(Action(self.player1, Card(1, 3)))
		self.game.apply_action(Action(self.player2, Card(2, 2)))
		self.game.round_end()

		completed_round = self.game.completed_rounds[1]
		self.assertEqual(completed_round.winning_action, Action(self.player2, Card(2, 2)))

		self.assertEqual(self.player1.cards, [])
		self.assertEqual(self.player2.cards, [])

	def test_get_winning_player(self):
		self.player1 = Player('Player 1', [Card(1, 4), Card(1, 3)])
		self.player2 = Player('Player 2', [Card(1, 2), Card(1, 1)])

		self.game.round_start()
		self.game.apply_action(Action(self.player1, Card(1, 4)))
		self.game.apply_action(Action(self.player2, Card(1, 2)))
		self.game.round_end()

		self.assertEqual(self.game.get_winner(), self.player1)

		self.game.round_start()
		self.game.apply_action(Action(self.player1, Card(1, 3)))
		self.game.apply_action(Action(self.player2, Card(1, 1)))
		self.game.round_end()

		self.assertEqual(self.game.get_winner(), self.player1)

if __name__ == '__main__':
	unittest.main()