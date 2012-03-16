#!/usr/bin/env python
def test_power_sum(n, p):
	sum, t = 0, n
	while t > 0:
		sum += (t % 10) ** p
		t /= 10
	return sum == n

power_sum = 0
for i in range(2, 1000000):
	if test_power_sum(i, 5):
		print i
		power_sum += i

print "Answer is", power_sum
