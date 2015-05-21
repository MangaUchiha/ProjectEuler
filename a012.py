#!/usr/bin/python

import math

def triangola(n):
	tri = 0
	for i in range(1,n):
		tri += i
	return tri

def divisi(n):
	nDiv = 0
	for i in range(1, int(1 + math.sqrt(n))):
		if(n%i == 0):
			nDiv += 2
	return nDiv

n = 0
i = 0

while divisi(n) < 501:
	n = triangola(i)
	i += 1
print str(i) + " : " + str(triangola(i)) + " : " + str(divisi(n))