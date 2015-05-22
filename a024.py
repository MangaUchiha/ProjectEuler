#!/usr/bin/python

done1 = 0
done2 = 0
done3 = 0
done4 = 0
done5 = 0
done6 = 0

def FromListToStr (lista):
	stringa = str(lista).strip("[]").replace("'", "").replace(" ", "").replace(",", "")
	return stringa

def ultimecrescenti(string):
	digits = [ "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
	result = ""
	filtered_digits = [x for x in digits if x not in list(string)]
	for j in filtered_digits:
		result += j
	return result

def next (string):
	if string == "9876543210":
		return None
	else:
		l = len(string)
		penultimacifra = string[l-2]
		inverse = string[:l-2] + string[l-1:] + penultimacifra
		if int(inverse) > int(string):
			return inverse
		elif int(string[l-3]) != 9 and done1 == 0:
			ultimacifra = str(int(string[l-3]) + 1)
			if int(ultimacifra) == int(string[l-4]) or int(ultimacifra) == int(string[l-6]) or int(ultimacifra) == int(string[l-7]) or int(ultimacifra) == int(string[l-8]) or int(ultimacifra) == int(string[l-9]) or int(ultimacifra) == int(string[l-10]):
				ultimacifra = str(int(ultimacifra) + 1)
			stringTagliata = string[:l-3]
			string = stringTagliata + ultimacifra
			string += ultimecrescenti(string)
			return string
		elif int(string[l-4]) != 9 and done2 == 0:
			ultimacifra = str(int(string[l-4]) + 1)
			if int(ultimacifra) == int(string[l-5]) or int(ultimacifra) == int(string[l-6]) or int(ultimacifra) == int(string[l-7]) or int(ultimacifra) == int(string[l-8]) or int(ultimacifra) == int(string[l-9]) or int(ultimacifra) == int(string[l-10]):
				ultimacifra = str(int(ultimacifra) + 1)
			stringTagliata = string[:l-4]
			string = stringTagliata + ultimacifra
			string += ultimecrescenti(string)
			global done1
			done1 = 1
			return string
		elif int(string[l-5]) != 9 and done3 == 0:
			ultimacifra = str(int(string[l-5]) + 1)
			if int(ultimacifra) == int(string[l-6]) or int(ultimacifra) == int(string[l-7]) or int(ultimacifra) == int(string[l-8]) or int(ultimacifra) == int(string[l-9]) or int(ultimacifra) == int(string[l-10]):
				ultimacifra = str(int(ultimacifra) + 1)
			stringTagliata = string[:l-5]
			string = stringTagliata + ultimacifra
			string += ultimecrescenti(string)
			global done2
			done2 = 1
			return string
		elif int(string[l-6]) != 9 and done4 == 0:
			ultimacifra = str(int(string[l-6]) + 1)
			if int(ultimacifra) == int(string[l-7]) or int(ultimacifra) == int(string[l-8]) or int(ultimacifra) == int(string[l-9]) or int(ultimacifra) == int(string[l-10]):
				ultimacifra = str(int(ultimacifra) + 1)
			stringTagliata = string[:l-6]
			string = stringTagliata + ultimacifra
			string += ultimecrescenti(string)
			global done3
			done3 = 1
			return string
		elif int(string[l-7]) != 9 and done5 == 0:
			ultimacifra = str(int(string[l-7]) + 1)
			if int(ultimacifra) == int(string[l-8]) or int(ultimacifra) == int(string[l-9]) or int(ultimacifra) == int(string[l-10]):
				ultimacifra = str(int(ultimacifra) + 1)
			stringTagliata = string[:l-7]
			string = stringTagliata + ultimacifra
			string += ultimecrescenti(string)
			global done4
			done4 = 1
			return string
		elif int(string[l-8]) != 9 and done6 == 0:
			ultimacifra = str(int(string[l-8]) + 1)
			if int(ultimacifra) == int(string[l-9]) or int(ultimacifra) == int(string[l-10]):
				ultimacifra = str(int(ultimacifra) + 1)
			stringTagliata = string[:l-8]
			string = stringTagliata + ultimacifra
			string += ultimecrescenti(string)
			global done5
			done5 = 1
			return string
		elif int(string[l-9]) != 9:
			ultimacifra = str(int(string[l-9]) + 1)
			if int(ultimacifra) == int(string[l-10]):
				ultimacifra = str(int(ultimacifra) + 1)
			stringTagliata = string[:l-9]
			string = stringTagliata + ultimacifra
			string += ultimecrescenti(string)
			global done6
			done6 = 1
			return string
		else:
			ultimacifra = str(int(string[l-10]) + 1)
			stringTagliata = string[:l-10]
			string = stringTagliata + ultimacifra
			string += ultimecrescenti(string)
			global done1
			global done2
			global done3
			global done4
			global done5
			global done6
			done1 = 0
			done2 = 0
			done3 = 0
			done4 = 0
			done5 = 0
			done6 = 0
			return string

counter = 1
seq = "0123456789"
print str(counter) + " : " + seq + "\n"
while counter <= 1000:
	seq = next(seq)
	counter += 1
	print str(counter) + " : " + seq + "\n"

