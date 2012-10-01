#!/usr/bin/env python
from utils import factors

def is_pandigital(n):
	match = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9
	digit_sum = 0
	while n > 0:
		digit_sum += n % 10
		n /= 10
	return match == digit_sum

