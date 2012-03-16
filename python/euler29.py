#!/usr/bin/env python

def distinct_terms(min, max):
	t = set() # set is used for the uniqification :)
	a, b = min, max
	for i in range(min, max + 1):
		for j in range(min, max + 1):
			t.add(a**j)
		a += 1
	return t

a, b = 2, 100
print "There are", len(distinct_terms(a, b)), "distinct terms " \
	  "between", a, "< a <", b, "and", a, "< b <", b
