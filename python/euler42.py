#!/usr/bin/env python

"""
The n^(th) term of the sequence of triangle numbers is given by,
t_(n) = 1/2n(n+1); so the first ten triangle numbers are:

	1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its
alphabetical position and adding these values we form a word value.
For example, the word value for SKY is 19 + 11 + 25 = 55 = t_(10). If the
word value is a triangle number then we shall call the word a triangle word.

Using euler42.txt, a 16K text file containing nearly two-thousand common
English words, how many are triangle words?
"""

def wordsum(word):
	return sum([ord(c) - ord('A') + 1 for c in word])

def trinum(n):
        if n & 1: return ((n / 2) + 1) * n
        else: return (n / 2) * (n + 1)

trinums = [trinum(n) for n in range(100)]

with open("../data/euler42.txt") as f:
	wordsums = [wordsum(n.strip('"')) for n in f.read().split(",")]

print sum([i in trinums for i in wordsums]), "words are triangle words."

