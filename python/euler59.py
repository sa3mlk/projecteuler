#!/usr/bin/env python
from collections import Counter
from itertools import permutations

def decrypt(ct, key):
	pt = ""
	for i, c in enumerate(ct):
		pt += chr(c ^ ord(key[i % len(key)]))
	return pt

def main():
	with open("../data/euler59.txt") as f:
		ct = map(int, f.read().split(","))

	counter = Counter(ct)
	commons = ([char for char, count in counter.most_common()][:3])

	# Most common letters that I can think of is " ", "e", "t" and "a"
	possible_keys = []
	for c in " eta":
		key = "".join(map(chr, [ord(c) ^ k for k in commons]))
		if key.isalpha():
			possible_keys.append(key)

	for keys in map(permutations, possible_keys):
		for key in keys:
			pt = decrypt(ct, key)
			print "{fill} Trying key \"{key}\" {fill}".format(fill="-" * 40, key="".join(key))
			print pt
			print "\nASCII sum is {sum}.\n".format(sum=sum(map(ord, pt)))

if __name__ == "__main__":
	main()
