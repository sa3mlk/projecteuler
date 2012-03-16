#!/usr/bin/env python

def next_perfect_number(n = 1):
	"""A perfect number is a number where all proper
	divisors is equal to the number.

	Yields the next perfect number from n
	"""
	while (True):
		pn = 0
		for i in range(1, (n / 2) + 1):
			if n % i == 0:
				pn += i
				if pn > n:
					break
		if pn == n:
			yield pn
		n += 1

def next_abundant_number(n = 1):
	"""An abundant number is a number where all proper
	divisors exceed the number

	Yields the next abundant number from n
	"""
	while (True):
		an = 0
		for i in range(1, (n / 2) + 1):
			if n % i == 0:
				an += i
		if an > n:
			yield n
		n += 1

i = 0
for n in next_perfect_number():
	print n
	i += 1
	if i > 20: break

