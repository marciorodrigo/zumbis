# -*- coding: utf-8 -*- 

a = float(input("Informe o primeiro número: "))
b = float(input("Informe o segundo número: "))
c = float(input("Informe o terceiro número: "))

menor = a

if menor > b:
	menor = b
	
if menor > c:
	menor = c

print "O menor valor é %f" %menor