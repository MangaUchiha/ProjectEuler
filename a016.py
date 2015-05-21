#!/usr/bin/python

c = str(2 ** 1000)
tot = 0

for i in range(0,len(c)):
	tot += int(c[i])
print tot
