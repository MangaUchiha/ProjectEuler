#!/usr/bin/python

digits = [ "0", "1", "2", "3", "4", "5", "6", "7", "8", "9" ]
numbers = []

for a in range(0,10):
	for b in range(1,10):
		for c in range(2,10):
			for d in range(3,10):
				for e in range(4,10):
					for f in range(5,10):
						for g in range(6,10):
							for h in range(7,10):
								for i in range(8,10):
									j = 9
									string = digits[a] + digits[b] + digits[c] + digits[d] + digits[e] + digits[f] + digits[g] + digits[h] + digits[i] + digits[j]
									numbers.append(string)

print len(numbers)
numbers = [int(x) for x in numbers]
numbers.sort()
print numbers[999999]