#!/usr/bin/env python
# Project Euler, problem 20. Calculate the number of digits in 100!
from math import pow

def factorial(n):
	if n == 0: return 1
	else: return n * factorial(n - 1)

x = factorial(100)
a = 0
while x > 0:
	a += x % 10;
	x /= 10

print "Answer is %d" % a
