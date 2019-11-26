from card_game import Dealer, MultiValCardGame

class TacticsAnalyser:
	def __init__(self, cards, players):
		self.dealer = Dealer(cards)
		self.players = players
		self.wins = None
		self.game = None

	def run(self, num_games):
		self.wins = dict.fromkeys(self.players, 0)
		for _ in range(num_games):
			self.setup_game()
			self.run_game()
			self.end_game()
		return self.get_results(num_games)

	def setup_game(self):
		self.game = MultiValCardGame(self.players)
		self.dealer.shuffle_cards()
		self.dealer.deal_to(self.players)

	def run_game(self):
		while(self.players[0].cards):
			self.game.round_start()
			self.run_round()
			self.game.round_end()

	def run_round(self):
		for player in self.players:
			action = player.tactic(self.game, player)
			self.game.apply_action(action)

	def end_game(self):
		winning_player = self.game.get_winner()
		self.wins[winning_player] = self.wins[winning_player] + 1

	def get_results(self, num_games):
		return [(player, player.tactic.__name__, self.wins[player] / num_games) for player in self.players]