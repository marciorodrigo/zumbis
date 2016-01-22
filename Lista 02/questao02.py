# -*- coding: utf-8 -*- 

ano = float(input("Informe o ano: "))

if ((ano % 4 == 0) and ((ano % 400 == 0) or (ano % 100 != 0))):
	print "O ano %d é bissexto" %ano
else:
	print "O ano %d não é bissexto" %ano