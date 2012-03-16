#!/usr/bin/env python
import operator

# A slightly efficient superset of primes
def primes_plus():
    yield 2
    yield 3
    i = 5
    while True:
        yield i
        if i % 6 == 1:
            i += 2
        i += 2

# Returns a dict d with n = produc p ^ d[p]
def get_prime_decomp(n):
    d = {}
    primes = primes_plus()
    for p in primes:
        while n % p == 0:
            n /= p
            d[p] = d.setdefault(p, 0) + 1
        if n == 1:
            return d

def num_divs(n):
    d = get_prime_decomp(n)
    powers_plus = map(lambda x: x + 1, d.values())
    return reduce(operator.mul, powers_plus, 1)

def trinum(n):
	if n & 1: return ((n / 2) + 1) * n
	else: return (n / 2) * (n + 1)

t, d, max_divs = 1, 0, 0
max = 500
while d < max:
    tri = trinum(t)
    d = num_divs(tri)
    t += 1 
    if d > max_divs:
        max_divs = d
        print "%d: %d" % (tri, d)

print "Answer is", trinum(t - 1)

