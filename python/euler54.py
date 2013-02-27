#!/usr/bin/env python
from collections import Counter

"""
In the card game poker, a hand consists of five cards and are ranked, from lowest to
highest, in the following way:

   * High Card: Highest value card.
   * One Pair: Two cards of the same value.
   * Two Pairs: Two different pairs.
   * Three of a Kind: Three cards of the same value.
   * Straight: All cards are consecutive values.
   * Flush: All cards of the same suit.
   * Full House: Three of a kind and a pair.
   * Four of a Kind: Four cards of the same value.
   * Straight Flush: All cards are consecutive values of same suit.
   * Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest value wins;
for example, a pair of eights beats a pair of fives (see example 1 below). But if two ranks
tie, for example, both players have a pair of queens, then highest cards in each hand are
compared (see example 4 below); if the highest cards tie then the next highest cards are
compared, and so on.

How many hands does Player 1 win?
"""

from collections import Counter

values = lambda h: sorted([c[0] for c in h])
suits = lambda h: sorted([c[1] for c in h])

def is_straight(h):
	straights = (
		"A2345", "23456", "34567", "45678", "56789",
		"6789T", "789TJ", "89TJQ", "9TJQK", "TJQKA"
	)
	return True if "".join(values(h)) in straights else False

def is_flush(h):
	if len(set(suits(h))) > 1:
		return False
	return True

def is_n_of_a_kind(h, n):
	counter = Counter(values(h))
	return counter.most_common()[0][1] == n

def is_two_pair(h):
	counter = Counter(values(h))
	c = counter.most_common()[:2]
	return c[0][1] == 2 and c[1][1] == 2

def is_full_house(h):
	counter = Counter(values(h))
	c = counter.most_common()[:2]
	return c[0][1] == 3 and c[1][1] == 2

def is_one_pair(h):
	return is_n_of_a_kind(h, 2)

def is_three_of_a_kind(h):
	return is_n_of_a_kind(h, 3)

def is_four_of_a_kind(h):
	return is_n_of_a_kind(h, 4)

def is_straight_flush(h):
	return True if is_flush(h) and is_straight(h) else False

def is_royal_flush(h):
	return True if "AJKQT" == "".join(values(h)) and is_flush(h) else False

def rank_hands(p1, p2):
	methods = (
		is_royal_flush, is_straight_flush, is_four_of_a_kind,
		is_full_house, is_flush, is_straight,
		is_three_of_a_kind, is_two_pair, is_one_pair
	)

	print "p1 = " + " ".join(p1)
	print "p2 = " + " ".join(p2)

	for m in methods:
		if m(p1) and not m(p2):
			return 1
		elif m(p2) and not m(p1):
			return 2

	v1 = "".join(values(p1))
	v2 = "".join(values(p2))

	print "High card"

	high_cards = "AKQJT98765432"

	for h in high_cards:
		if h in v1 and h not in v2:
			return 1
		elif h in v2 and h not in v1:
			return 2

def main():
	hands = []
	with open("../data/euler54.txt") as f:
		for l in f.readlines():
			l = l.strip()
			hands.append((l[0:14].split(" "), l[15:].split(" ")))

	for p1, p2 in hands:
		winner = rank_hands(p1, p2)
		print "The winner is player {0}".format(winner)
		raw_input()

if __name__ == "__main__":
	main()

