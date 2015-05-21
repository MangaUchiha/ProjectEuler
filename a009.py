#!/usr/bin/python

m = 2
n = 1

for m in range(1,998):
	for n in range (1,998):
		a = m**2 - n**2
		b = 2 * m * n
		c = m**2 + n**2
		if (a + b + c == 1000) and (a > 0) and (b > 0) and (c > 0):
			prodotto = a * b * c
			print prodotto
