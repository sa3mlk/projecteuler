#!/usr/bin/env python

def next(n):
	sum = 0
	while n > 0:
		sum += (n % 10) ** 2
		n /= 10
	return sum

def number_chain(n):
	while True:
		p = n
		n = next(n)
		if n == 1:
			return False
		if n == 89:
			return True

num_arrivals = 0
for i in range(1, (10**7) + 1):
	if number_chain(i):
		num_arrivals += 1

print "Answer is", num_arrivals
