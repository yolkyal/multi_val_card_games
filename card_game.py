import random


class Player:
	def __init__(self, _id, cards=None):
		self._id = _id
		self.cards = cards if cards else []

	def __eq__(self, other):
		return self._id == other._id

	def __hash__(self):
		return hash(self._id)

	def __str__(self):
		return self._id

	def __repr__(self):
		return self.__str__()


class Action:
	def __init__(self, player, card):
		self.player = player
		self.card = card

	def __eq__(self, other):
		return type(other) == Action and self.player == other.player and self.card == other.card

	def __hash__(self):
		return hash((player, card))

	def __str__(self):
		return str(self.player) + ':' + str(self.card)

	def __repr__(self):
		return self.__str__()


class Dealer:
	def __init__(self, cards):
		self.cards = cards

	def shuffle_cards(self, num_swaps=1000):
		for i in range(num_swaps):
			rand_1 = random.randint(0, len(self.cards) - 1)
			rand_2 = random.randint(0, len(self.cards) - 1)
			tmp = self.cards[rand_1]
			self.cards[rand_1] = self.cards[rand_2]
			self.cards[rand_2] = tmp

	def deal_to(self, players):
		player_i = 0
		for card in self.cards:
			players[player_i].cards += [card]
			player_i = (player_i + 1) % len(players)


class MultiValCardGame:
	def __init__(self, players):
		self.players = players
		self.completed_rounds = []
		self.active_round = None

	def round_start(self):
		self.active_round = self.MultiValCardGameRound()

	def round_end(self):
		self.completed_rounds += [self.active_round]
		self.active_round = None

	def get_actions(self, player):
		return [Action(player, card) for card in player.cards]

	def apply_action(self, action):
		if not self.active_round:
			raise NoActiveRoundException()
		if action.card in action.player.cards:
			action.player.cards.remove(action.card)
			self.active_round.apply_action(action)
		else:
			raise ValueError(str(action.player) + ' does not have ' + str(action.card))

	def __str__(self):
		return str([(str(player), [str(card) for card in player.cards]) for player in self.players])

	class MultiValCardGameRound:
		def __init__(self):
			self.actions = []
			self.winning_action = None

		def apply_action(self, action):
			self.actions += [action]
			if self.winning_action == None or (action.card > self.winning_action.card):
				self.winning_action = action


class NoActiveRoundException(Exception):
	pass