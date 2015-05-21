#!/usr/bin/python

def factor(n):
	f = 1
	for m in range(1,n+1):
		f *= m
	return f

p = factor(40)/(factor(20)**2)
print p