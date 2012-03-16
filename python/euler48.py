#!/usr/bin/env python

"""
The series, 1^(1) + 2^(2) + 3^(3) + ... + 10^(10) = 10405071317.
Find the last ten digits of the series,
	1^(1) + 2^(2) + 3^(3) + ... + 1000^(1000).
"""

from sys import setrecursionlimit
setrecursionlimit(1002)

def f(n):
	if not n: return 0
	else: return n**n + f(n - 1)

print "Answer is %d" % (f(1000) % 10**10)
