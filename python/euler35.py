#!/usr/bin/env python

"""
The number, 197, is called a circular prime because all rotations of the
digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100:
	2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""

from utils import reverse, num_digits, is_prime

max = 10**6 

def next_prime():
	n = 1
	while True:
		if is_prime(n):
			yield n
		n = n + 1

def rotate(n):
	r, n = n % 10, n / 10
	return n + r * 10 ** num_digits(n)

primes = []
for n in next_prime():
	if n > max: break
	primes.append(n)

num_circular = 0
for p in primes:
	def test_circular(n):
		for i in range(0, num_digits(n)):
			if not is_prime(n):
				return False
			n = rotate(n)
		return True	
	if test_circular(p):
		num_circular += 1

print "There are", num_circular, "primes below", max
