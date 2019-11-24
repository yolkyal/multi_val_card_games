import functools
import random
import cards
from card_game import Action


def tactic_play_highest_card(game, player):
	return Action(player, cards.get_highest(player.cards))


def tactic_play_lowest_card(game, player):
	return Action(player, cards.get_lowest(player.cards))


def tactic_play_random_card(game, player):
	return Action(player, cards.get_random(player.cards))


def tactic_play_lowest_winning_card(game, player):
	if game.active_round.winning_action:
		winning_card = game.active_round.winning_action.card
		worst_winning_card = None
		for card in player.cards:
			if card > winning_card and (worst_winning_card is None or card < worst_winning_card):
				worst_winning_card = card
		if worst_winning_card:
			return Action(player, worst_winning_card)
		else:
			return tactic_play_lowest_card(game, player)

	return tactic_play_random_card(game, player)