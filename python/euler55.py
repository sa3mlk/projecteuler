#!/usr/bin/env python
from utils import reverse, is_palindrome

def is_lychrel(n, i = 50):
	for j in range(i):
		n = n + reverse(n)
		if is_palindrome(n):
			return False
	return True

num_lychrel = 0
for i in range(10000):
	if is_lychrel(i):
		num_lychrel += 1

print "There is", num_lychrel, "Lychrel numbers below ten-thousand"

