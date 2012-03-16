#!/usr/bin/env python
def fibonacci():
	a, b, i = 0, 1, 0
	while 1:
		yield a, i
		a, b, i = b, a + b, i + 1

for x, i in fibonacci():
	if x >= 10**(1000 - 1):
		print "Answer is %d" % i
		break;
