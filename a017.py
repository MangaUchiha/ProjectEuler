#!/usr/bin/python

unity = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
dec = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

def small(n):
	m = unity[n-1]
	return m

def big(n):
	m = dec[n-2]
	return m

def char(n):
	m = str(n)
	l = len(m)
	letters = str("")
	if l == 4:
		letters = "one thousand"
	else:
		if l >= 3:
			letters += small(int(m[0])) + "hundred"
			if m.endswith("00"):
				return letters
			else:
				letters += " " + "and" + " "
		if l >= 2:
			if int(m[l-2]) == 1:
				lasttwo = int(m[l-2] + m[l-1])
				letters += small(lasttwo)
				return letters
			else:
				if int(m[l-2]) != 0:
					letters += big(int(m[l-2]))
					if m.endswith("0"):
						return letters
		if l >= 1:
			letters += small(int(m[l-1]))
	return letters

def nospace(string):
	newstring = string.replace(" ","")
	return newstring

n = 0
tot = 0

for n in range(1,1001):
	ch = char(n)
	no = nospace(ch)
	tot += len(no)
	print n
	print ch
	print no

print tot
