#!/usr/bin/env python

"""
Some positive integers n have the property that the sum [ n + reverse(n) ] consists entirely of odd (decimal) digits. For instance, 36 + 63 = 99 and 409 + 904 = 1313. We will call such numbers reversible; so 36, 63, 409, and 904 are reversible. Leading zeroes are not allowed in either n or reverse(n).

There are 120 reversible numbers below one-thousand.

How many reversible numbers are there below one-billion (10^(9))?
"""

from utils import reverse

def is_all_odd(n):
	while n > 0:
		if n & 1 == 0:
			return False
		n /= 10
	return True

def is_reversible(n):
	if n % 10 == 0:
		return False
	r = reverse(n)
	if r % 10 == 0:
		return False
	else:
		if r + n & 1 == 0:
			return False
		else:
			return is_all_odd(n + r)

i, num_reversible = 0, 0
while i < 1000000:
	num_reversible += is_reversible(i)
	i += 1

print "Answer is", num_reversible

"""
num_reversible = sum([is_reversible(i) for i in xrange(10**9)])
print "Answer is", num_reversible

givez
Macintosh:projecteuler jonasg$ time ./euler145.py 
Traceback (most recent call last):
  File "./euler145.py", line 32, in <module>
    num_reversible = sum([is_reversible(i) for i in xrange(10**9)])
MemoryError

real	78m0.968s
user	73m39.828s
sys	0m15.685s
"""
