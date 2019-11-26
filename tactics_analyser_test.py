import unittest
from cards import CardGenerator
from card_game import Player
from tactics_methods import tactic_play_random_card
from tactics_analyser import TacticsAnalyser


class TestTacticsMethods(unittest.TestCase):

	def test_1000_random_tactic_executions(self):
		cards = CardGenerator.generate([1, 2], [1, 2, 3, 4, 5])
		player1 = Player('Player 1', cards=[], tactic=tactic_play_random_card)
		player2 = Player('Player 2', cards=[], tactic=tactic_play_random_card)
		tactics_analyser = TacticsAnalyser(cards, [player1, player2])
		results = tactics_analyser.run(1000)
		self.assertEqual(len(results), 2)

if __name__ == '__main__':
	unittest.main()