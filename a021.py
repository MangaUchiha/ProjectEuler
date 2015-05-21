#!/usr/bin/python

def sommaDiv(n):
	s = 0
	for i in range(1,n):
		if n % i == 0:
			s += i
	return s

tot = 0
for i in range(1,10001):
	s = sommaDiv(i)
	if sommaDiv(s) == i and s != i:
		tot += i + s
tot = tot // 2
print tot