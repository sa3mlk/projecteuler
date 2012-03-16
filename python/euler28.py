#!/usr/bin/env python
def spiral_sum(size):
	a, d, sum, i = 2, 5, 0, 1
	while i < (size**2) + 1:
		d -= 1
		if d == 0:
			a, d = a + 2, 4
		sum, i = sum + i, a + i
	return sum

print "Spiral sum of 1001x1001 is", spiral_sum(1001)
