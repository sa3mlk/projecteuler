#!/usr/bin/env python
from math import factorial

min, max = 3, 99999

def factorion(n):
	while n < max:
		s, f = str(n), 0
		for d in range(0, len(s)):
			f += factorial(int(s[d]))
		if n == f:
			yield n
		n += 1

print "The Factorion sum is", sum(factorion(min)), "from", min, "< n <", max

