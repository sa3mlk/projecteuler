#!/usr/bin/env python

# First measure how long range we should use
c, total_range = 0, 1
while c < 1000000:
    c += len(str(total_range))
    total_range += 1

# A very naive and slow solution
d = reduce(lambda x, y: x + y, [str(x) for x in xrange(0, total_range)])

# All values for 'd'
ds = [10**i for i in range(0, 7)]

# Now multiply all digits
answer = 1
for index in ds:
    answer *= int(d[index])

print "The answer is", answer

