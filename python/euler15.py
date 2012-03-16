#!/usr/bin/env python
from math import factorial as f

def num_grid_combinations(w, h):
	return f(w + h) / (f(w) * f(h))

print "Answer is", num_grid_combinations(20, 20)
