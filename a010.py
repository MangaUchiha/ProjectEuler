#!/usr/bin/python
import math
primi = [2,3,5,7]
tot=0

def isPrime(n):
	sqr=int(math.sqrt(n))
	for el in primi:
		if el <= sqr:
			if (n%el) == 0:
				return False
		else:
			return True
	return True

for n in range (11,2000000):
	if (n%2) != 0:
		if isPrime(n):
			primi.append(n)

for el in primi:
	tot += el

print tot