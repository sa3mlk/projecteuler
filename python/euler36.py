#!/usr/bin/env python
from  utils import is_palindrome

def is_binary_palindrome(n):
	s = str(bin(n))[2:]
	return s == s[::-1]

sum = 0
for i in range(1, 1000000):
	if is_palindrome(i) and is_binary_palindrome(i):
		print i, bin(i)[2:]
		sum += i

print "Answer is", sum
