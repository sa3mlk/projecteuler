#!/usr/bin/env python
from utils import is_prime
from itertools import permutations

def main():
	pandigital_numbers = [permutations(xrange(1, x)) for x in xrange(3, 9)]
	primes = []
	for nums in pandigital_numbers:
		for n in nums:
			pn = int("".join([str(x) for x in n]))
			if is_prime(pn):
				primes.append(pn)
	print "The largest 1 to n pandigital prime is {prime}.".format(prime=max(primes))

if __name__ == "__main__":
	main()

