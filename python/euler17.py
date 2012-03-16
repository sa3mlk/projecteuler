#!/usr/bin/env python
import utils

words = (0, 'zero'), (1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), \
	(5, 'five'), (6, 'six'), (7, 'seven'), (8, 'eight'), (9, 'nine'), \
	(10, 'ten'), (11, 'eleven'), (12, 'twelve'), (13, 'thirteen'), \
	(14, 'fourteen'), (15, 'fifteen'), (16, 'sixteen'), (17, 'seveneen'), \
	(18, 'eighteen'), (19, 'nineteen'), (20, 'twenty'), (30, 'thirty'), \
	(40, 'fourty'), (50, 'fifty'), (60, 'sixty'), (70, 'seventy'), \
	(80, 'eighty'), (90, 'ninety'), (100, 'hundred'), (1000, 'thousand')

# 102 = one hundred and two
# 100 = one hundred
# 1 = one

def ntos(n):
	def get(n):
		for i, w in words:
			if i == n:
				return i
		return None

	if n >= 100 and n <= 999:
		print words[n / 100][1],
		print get(n/(n/100))[1],
		if n % 100:
			r = get(n % 100)
			if r: print "and", r[1]

n = 221
ntos(n)
