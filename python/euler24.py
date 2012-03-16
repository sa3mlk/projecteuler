#!/usr/bin/env python

"""
A permutation is an ordered arrangement of objects. For example, 3124 is one
possible permutation of the digits 1, 2, 3 and 4. If all of the permutations
are listed numerically or alphabetically, we call it lexicographic order.
The lexicographic permutations of 0, 1 and 2 are:

	012  021  102  120  201  210

What is the millionth lexicographic permutation of the
digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""

def permute(k, s):
	for j in range(2, len(s)):
		i = (k % j)
		s[i], s[j] = s[j], s[i]
		k = k / j
	return s

v = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
s = []

for i in range(1000001):
	v = permute(i, v)
	s.append(list(v))

print "Permutations done"

s.sort()
print s[-1]
