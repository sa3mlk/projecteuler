#!/usr/bin/env python

"""
The number 3797 has an interesting property. Being prime itself, it is
possible to continuously remove digits from left to right, and remain prime
at each stage: 3797, 797, 97, and 7. Similarly we can work from right to
left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left
to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""

from utils import is_prime, num_digits

def ltrunc(n):
	o = num_digits(n) - 1
	d = 10 ** (num_digits(n) - 1)
	while num_digits(n) != o:
		n -= d
	return n

def rtrunc(n):
	return n / 10

def next_prime():
	i = 10
	while True:
		if is_prime(i):
			yield i
		i += 1

def is_prime_truncatable(n):
	right = n
	while num_digits(right) > 0:
		if not is_prime(right):
			return False
		right = rtrunc(right)
	left = n
	while num_digits(left) > 0:
		if not is_prime(left):
			return False
		left = ltrunc(left)
	return True

num_found = 0
truncatable_prime_sum = 0
for i in next_prime():
	if is_prime_truncatable(i):
		num_found += 1
		print i, "is truncatable (%d found)" % num_found
		truncatable_prime_sum += i
		if num_found == 11:
			break

print "Answer is", truncatable_prime_sum

