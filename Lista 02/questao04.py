# -*- coding: utf-8 -*- 

a = float(input("Informe o primeiro número: "))
b = float(input("Informe o segundo número: "))
c = float(input("Informe o terceiro número: "))

maior = a

if maior < b:
	maior = b
	
if maior < c:
	maior = c

print "O maior valor é %f" %maior
