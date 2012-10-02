#!/usr/bin/env python
"""Utils library."""

from math import sqrt

#m = 11 * 19 # large primes should be used
xi = 20300713
#xi = 9
m = 14025256

def bbs():
	"""Blum Blum Shub algorithm.

	Return a pseudo random generated number.
	"""
	global xi
	xi = (xi ** 2) % m
	return xi

def is_palindrome(n):
	"""Test for palindromic number.

	Return True if the number is a palindrome.
	"""
	t, r = n, 0
	while (t > 0):
		r = r * 10 + t % 10
		t /= 10
	return n == r

def is_prime(n):
	"""Test for prime number.

	Return True if n is a prime number, otherwise False.
	"""
	if n == 1: return False
	if n == 2: return True
	if n & 1 == 0: return False
	for i in range(2, int(sqrt(n)) + 1):
		if n % i == 0:
			return False;
	return True;

def reverse(n):
	"""Reverse number.

	Reverse the number using radix 10.
	"""
	r = 0
	while n > 0:
		r, n = r + n % 10, n / 10
		r = r * 10
	return r / 10

def num_digits(n):
	"""Number of digits.

	Return the number of digits in n using radix 10.
	"""
	d = 0
	while n > 0:
		n, d = n / 10, d + 1
	return d

def factors(n):
	"""Find factors of a given number.

	Return a list of all factors.
	"""
	# 1 and n are automatically factors of n.
	fact = [1, n]
	# Starting at 2 as we have already dealt with 1
	check = 2
	# Calculate the square root of n and use this as the
	# limit when checking if a number is divisible as
	# factors above sqrt(n) will already be calculated as 
	# the inverse of a lower factor IE. finding factors of
	# 100 only need go up to 10 (sqrt(100)=10) as factors
	# such as 25 can be found when 5 is found to be a
	# factor 100/5=25
	rootn = sqrt(n)
	while check < rootn:
		if n % check == 0:
			fact.append(check)
			fact.append(n / check)
		check += 1
	if rootn == check:
		fact.append(check)
	return fact

