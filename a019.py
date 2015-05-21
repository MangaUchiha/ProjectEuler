#!/usr/bin/python

daysinmonth = {
	0 : 31,
	1 : 28,
	2 : 31,
	3 : 30,
	4 : 31,
	5 : 30,
	6 : 31,
	7 : 31,
	8 : 30,
	9 : 31,
	10 : 30,
	11 : 31
}

counter = 0
now = 365%7
for j in range(1901,2001):
	for i in daysinmonth:
		now += daysinmonth[i]
		if i == 2 and j%4 == 0 and j%100 != 0:
			now += 1
		if now % 7 == 6:
			counter += 1
print counter