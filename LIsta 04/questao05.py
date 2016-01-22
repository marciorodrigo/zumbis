# -*- coding: utf-8 -*- 

a = int(input("Informe o primeiro número: "))
b = int(input("Informe o segundo número: "))

print ("O MDC de %d e %d é " % (a, b)),

while a:
	a, b = b % a, a
	
print ("%d" % b)