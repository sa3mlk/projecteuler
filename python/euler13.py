#!/usr/bin/env python

"""
Work out the first ten digits of the sum of the one-hundred 50-digit
numbers in the file euler13.txt
"""

from __future__ import with_statement

def num_digits(a):
	i = 0
	while a > 0:
		a, i = a / 10, i + 1
	return i

with open("../data/euler13.txt") as f:
	a = 0
	for line in f:
		a = a + int(line)
	print "Answer is", (a / 10**(num_digits(a) - 10))
