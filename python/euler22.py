#!/usr/bin/env python

"""
Using euler22.tx , a 46K text file containing over five-thousand first names,
begin by sorting it into alphabetical order. Then working out the
alphabetical value for each name, multiply this value by its alphabetical
position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is
worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN
would obtain a score of 938 x 53 = 49714.

What is the total of all the name scores in the file?
"""

with open("../data/euler22.txt") as f:
	names = sorted([n.strip('"') for n in f.read().split(",")])

def score(name, pos):
	t = 0
	for c in name:
		t += ord(c) - ord('A') + 1
	return pos * t

i, total = 1, 0
for name in names:
	total += score(name, i)
	i += 1

print "The total is", total
