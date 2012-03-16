#!/usr/bin/env python
from operator import itemgetter

# This is a really ugly and slow hack, there are for sure a zillion
# ways to make this more effective, or perhaps an algorithm to get
# the number of recurring digits in the fraction
def num_recurring(d):
    s = "9"
    c = 1
    while True:
        n = int(s)
        if n % d == 0:
            return c
        s += "9"
        if int(s) % d == n % d:
            return c
        c += 1
        if c > 1000:
            return 0

nums = [(d, num_recurring(d)) for d in range(900, 1000)]
answer = max(nums, key=itemgetter(1))
print "Answer is %d which have %d divisors" % (answer[0], answer[1])

