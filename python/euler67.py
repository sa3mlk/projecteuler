#!/usr/bin/env python

tri = []
with open("../data/triangle.txt") as f:
	for row in ([l.rstrip("\r\n").split(" ") for l in f]):
		tri.append([int(c) for c in row])

maxsum = 0
for i in range(1, len(tri)):
	for j in range(0, len(tri[i])):
		if j == 0:
			tri[i][j] += tri[i - 1][j]
		elif j == len(tri[i]) - 1:
			tri[i][j] += tri[i - 1][len(tri[i - 1]) - 1]
		else:
			tri[i][j] += max(tri[i - 1][j], tri[i - 1][j - 1])
		if i == len(tri) - 1:
			if tri[i][j] > maxsum: maxsum = tri[i][j]

print "The maximum sum is", maxsum
