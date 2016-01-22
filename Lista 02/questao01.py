# -*- coding: utf-8 -*- 

a = float(input("Informe o primeiro lado: "))
b = float(input("Informe o segundo lado: "))
c = float(input("Informe o terceiro lado: "))

if (abs(b - c) > a) or (a > b + c):
	print "Não é um triângulo"
else:
	print("É um triângulo "),
	
	if (a == b) and (a == c):
		print "equilátero"
	elif b == c:
		print "isóceles"
	else:
		print "escaleno"
	