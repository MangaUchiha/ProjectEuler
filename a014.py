#!/usr/bin/python

def Collatz(n):
	if n % 2 == 0:
		i = n // 2
	else:
		i = 3 * n +1
	return i

maxn = 0
maxcounter = 0

for n in range(1,1000000):
	counter = 3
	m = Collatz(n)
	while Collatz(m) != 1:
		m = Collatz(m)
		counter += 1
	if counter > maxcounter:
		maxcounter = counter
		maxn = n
print maxn