# -*- coding: utf-8 -*- 


from math import sqrt


num = int(input("Informe o número: "))

found = False
for i in range(1, int(sqrt(num)) + 1):
	res = i * (i + 1) * (i + 2)
	if (res == num):
		found = True
		print i, i + 1, i + 2
		break

if not found:
	print ("%d não é triangular" % num)