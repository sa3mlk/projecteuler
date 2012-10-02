#!/usr/bin/env python
"""
We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once; for example, the 5-digit number, 15234, is
1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 x 186 = 7254, containing
multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can
be written as a 1 through 9 pandigital.
HINT: Some products can be obtained in more than one way so be sure to only
include it once in your sum.
"""
from utils import factors, num_digits

def is_pandigital(n):
	digit_bits = 0
	while n > 0:
		bit = 1 << (n % 10)
		# First check is the bit is already set, if set the number is not
		# a pandigital number.
		if digit_bits & bit:
			return False
		# OR in our unique bit.
		digit_bits |= bit
		# Continue to next digit
		n /= 10
	# If the number was pandigital bits 1-9 should be set.
	return digit_bits == 0x3fe

def concat_numbers(a, b, c):
	return a*(10**(num_digits(b) + num_digits(c))) + b*(10**num_digits(c)) + c

def main():
	pandigital_numbers = set()
	for p in xrange(1, 10000):
		f = factors(p)
		l = len(f) - 1 if len(f) & 1 else len(f)
		for a, b in [(f[i], f[i+1]) for i in xrange(0, l, 2)]:
			n = concat_numbers(a, b, p)
			if is_pandigital(n):
				pandigital_numbers.add(p)
				print "{0} is pandigital since {1}*{2}={3}".format(n, a, b, p)

	print "The answer is", sum(pandigital_numbers)

if __name__ == "__main__":
	main()

