#!/usr/bin/env python
"""Utils library."""

from math import sqrt

#m = 11 * 19 # large primes should be used
xi = 20300713
#xi = 9
m = 14025256

def bbs():
	"""Blum Blum Shub algorithm

	Return a pseudo random generated number
	"""
	global xi
	xi = (xi ** 2) % m
	return xi

def is_palindrome(n):
	"""Test for palindromic number

	Return True if the number is a palindrome
	"""
	t, r = n, 0
	while (t > 0):
		r = r * 10 + t % 10
		t /= 10
	return n == r

def is_prime(n):
	"""Test for prime number

	Return True if n is a prime number, otherwise False
	"""
	if n == 1: return False
	if n == 2: return True
	if n & 1 == 0: return False
	for i in range(2, int(sqrt(n)) + 1):
		if n % i == 0:
			return False;
	return True;

def reverse(n):
	"""Reverse number

	Reverse the number using radix 10
	"""
	r = 0
	while n > 0:
		r, n = r + n % 10, n / 10
		r = r * 10
	return r / 10

def num_digits(n):
	"""Number of digits

	Return the number of digits in n using radix 10
	"""
	d = 0
	while n > 0:
		n, d = n / 10, d + 1
	return d

