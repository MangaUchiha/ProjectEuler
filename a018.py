#!/usr/bin/python

s = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""
array = s.split("\n")

for i in range(0,len(array)):
	array[i] = array[i].split(" ")
	for j in range(0,len(array[i])):
		array[i][j] = int(array[i][j])

max = 0

for a in range(0,len(array[0])):
	for b in range(a, a+2):
		for c in range(b, b+2):
			for d in range(c, c+2):
				for e in range(d, d+2):
					for f in range(e, e+2):
						for g in range(f, f+2):
							for h in range(g, g+2):
								for i in range(h, h+2):
									for j in range(i, i+2):
										for k in range(j, j+2):
											for l in range(k, k+2):
												for m in range(l, l+2):
													for n in range(m, m+2):
														for o in range(n, n+2):
															tot = (array[0][a] +
																array[1][b] +
																array[2][c] +
																array[3][d] +
																array[4][e] +
																array[5][f] +
																array[6][g] +
																array[7][h] +
																array[8][i] +
																array[9][j] +
																array[10][k] +
																array[11][l] +
																array[12][m] +
																array[13][n] +
																array[14][o])
															if tot > max:
																max = tot
print max

