#!/usr/bin/env python

"""
Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0,
where each "_" is a single digit.
"""

from math import sqrt

def match(a):
	i = 10
	while a > 0:
		a, i = a / 100, i - 1
		if a % 10 != i:
			return False
	return True

n = int(sqrt(1929394959697989999)) + 1

i = 0
while not match(n * n):
	n, i = n - 1, i + 1

print "Answer is", n
print "%d iterations" % i

