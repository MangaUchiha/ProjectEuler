#!/usr/bin/python

def factor(n):
	f = 1
	for i in range(1,n+1):
		f *= i
	return f

def sumdigits(n):
	s = str(n)
	tot = 0
	for i in range(0,len(s)):
		tot += int(s[i])
	return tot

c = 100
x = sumdigits( factor(c))
print x